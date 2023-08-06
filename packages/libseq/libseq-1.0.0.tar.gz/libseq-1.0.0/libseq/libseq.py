#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:23:09 2018

@author: antony
"""

import collections
import numpy as np
import libbam
import libdna
import struct
import os
import s3fs

#SAMTOOLS='/ifs/scratch/cancer/Lab_RDF/abh2138/tools/samtools-1.8/bin/samtools'
SAMTOOLS = '/ifs/scratch/cancer/Lab_RDF/abh2138/tools/samtools-0.1.19/samtools'

CHRS = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20,', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM']
BIN_WIDTHS = {100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000}
POWER = {100:2, 1000:3, 10000:4, 100000:5, 1000000:6, 10000000:7, 100000000:8, 1000000000:9}

MIN_BIN_WIDTH = 100

MAGIC_NUMBER_OFFSET_BYTES = 0
BIN_SIZE_OFFSET_BYTES = MAGIC_NUMBER_OFFSET_BYTES + 4
BIN_WIDTH_OFFSET_BYTES = BIN_SIZE_OFFSET_BYTES + 1
N_BINS_OFFSET_BYTES = BIN_WIDTH_OFFSET_BYTES + 4
BINS_OFFSET_BYTES = N_BINS_OFFSET_BYTES + 4

NO_DATA = np.zeros(0, dtype=int)

class BinCountWriter(object):
    def __init__(self, bam, genome, bin_width, mode='max', samtools=SAMTOOLS):
        self.bam = bam
        self.dir = os.path.dirname(os.path.abspath(bam))
        self.genome = genome
        self.samtools = samtools
        self.power = POWER[bin_width]
        self.bin_width = bin_width
        self.mode = mode
        # cache counts
        self.read_map = np.zeros(280000000, dtype=int)
        self.bin_map = collections.defaultdict(int)
        self.sum_c = 0
    
    
    def _reset(self):
        self.read_map.fill(0)
        self.bin_map.clear()
    
    
    def _write(self, chr):
        if "_" in chr:
            # only encode official chr
            return
        
        max_i = np.max(np.where(self.read_map > 0))
        max_bin = max_i // self.bin_width
        bins = max_bin + 1
        
        block_map = np.zeros(bins, dtype=int)
        
        i = 0
        
        for b in range(0, bins):
            if self.mode == 'count':
                c = self.bin_map[b]
            elif self.mode == 'max':
                c = np.max(self.read_map[i:(i + self.bin_width)])
            else:
                # mean reads per bin
                c = int(round(np.floor(np.mean(self.read_map[i:(i + self.bin_width)]))))
            
            block_map[b] = c
            
            self.sum_c += c
            
            i += self.bin_width
            
        bin_size_bits = 8
        maxc = 0
        
        for c in block_map:
            if c > 255:
                bin_size_bits = 16
            
            if c > 65535:
                bin_size_bits = 32
                
            if c > maxc:
                maxc = c
        
        print('Blocks', block_map.size)
        print('Block size', bin_size_bits, maxc)
        
        out = os.path.join(self.dir, '{}.{}.{}bw.{}bit.{}.bc'.format(chr, self.genome, self.power, bin_size_bits, self.mode))
        
        print('Writing to {}...'.format(out))
        
        f = open(out, 'wb')
        f.write(struct.pack('>I', 42))
        # Write the bin size in bytes, either 1, 2, or 4
        f.write(struct.pack('>B', bin_size_bits // 8))
        f.write(struct.pack('>I', self.bin_width))
        # so we know how many bytes are used to represent a count
        #f.write(struct.pack('B', size_in_bytes))
        #f.write(struct.pack('I', max_i))
        #f.write(bytes(read_map))
        
        f.write(struct.pack('>I', len(block_map)))
        
        if bin_size_bits == 8:
            for c in block_map:
                f.write(struct.pack('>B', c))
        elif bin_size_bits == 16:
            for c in block_map:
                f.write(struct.pack('>H', c))
        else:
            for c in block_map:
                f.write(struct.pack('>I', c))
                
        f.close()
    
    
    def _write_count(self, reads):
        f = open(os.path.join(self.dir, 'reads.{}.{}.bc'.format(self.genome, self.mode)), 'wb')
        f.write(struct.pack('>I', reads))
        f.close()
        
        #f = open(os.path.join(self.dir, 'bc.reads.{}.{}.txt'.format(self.genome, self.mode)), 'w')
        #f.write(str(reads))
        #f.close()
        
        #f = open(os.path.join(self.dir, 'counts.{}.{}bw.{}.bc'.format(self.genome, self.power, self.mode)), 'wb')
        #f.write(struct.pack('>I', self.sum_c))
        #f.close()
        
        #f = open(os.path.join(self.dir, 'bc.counts.{}.{}bw.{}.txt'.format(self.genome, self.power, self.mode)), 'w')
        #f.write(str(self.sum_c))
        #f.close()
    
    
    def write(self, chr):
        sam = libbam.BamReader(self.bam, samtools=self.samtools)
        
        # reset the counts
        self._reset()
        
        self.sum_c = 0
        
        c = 0
        
        started = False
        
        for read in sam:
            if read.chr == chr:
                started = True
            else:
                if started:
                    # We can stop as we are no longer on this chr
                    break
                else:
                    # until we find the chr, skip processing the read
                    continue
            
            #for i in range(read.pos, read.pos + read.length):
            #    read_map[i] += 1 #.add(read.qname)
            
            self.read_map[read.pos:(read.pos + read.length)] += 1
            
            if c % 100000 == 0:
                print('Processed', str(c), 'reads...')
          
            c += 1
            
        if c == 0:
            return
        
        self._write(chr)
    
    
    def write_all(self):
        sam = libbam.BamReader(self.bam, samtools=self.samtools)
        
        chr = ''
        c = 0
        
        self.sum_c = 0
        
        reads = 0

        for read in sam:
            if read.chr != chr:
                if c > 0:
                    self._write(chr)
                
                self._reset()
                c = 0
                chr = read.chr
                
                print('Processing', chr, '...')
            
            
            
            if self.mode == 'count':
                sb = read.pos // self.bin_width
                eb = (read.pos + read.length - 1) // self.bin_width
                
                for b in range(sb, eb + 1):
                    self.bin_map[b] += 1
            
            self.read_map[read.pos:(read.pos + read.length)] += 1
            
            
            if c % 100000 == 0:
                print('Processed', str(c), 'reads...')
          
            reads += 1
            c += 1

            
        # Process what is remaining
        if c > 0:
            self._write(chr)
            
        self._write_count(reads)
            

class BinCountReader(object):
    def __init__(self, dir, genome, mode='max'):
        self._dir = dir
        self.genome = genome
        self.mode = mode
        
        self.file_map = collections.defaultdict(lambda: collections.defaultdict(str))
        self.bin_size_map = collections.defaultdict(lambda: collections.defaultdict(int))
        self._reads = -1
        
        
    def _get_file(self, chr, power):
        if power not in self.file_map[chr]:
            # Need to search for exact chr within file otherwise chr1 can map
            # to chr10 etc.
            s = chr + '.'
            p = '{}bw'.format(power)
            
            for file in os.listdir(self._dir):
                if s in file and self.genome in file and p in file and self.mode in file:
                    self.file_map[chr][power] = file #os.path.join(self.dir, file)
                    break
                
        return self.file_map[chr][power]
    
    def _read_data(self, file, n, seek=0):
        f = open(os.path.join(self._dir, file), 'rb')
        f.seek(seek)
        data = f.read(n)
        f.close()
        return data
    
    def _get_magic_num(self, file):
        data = self.read(file, 4)
        
        # return 42
        return struct.unpack('>I', data)[0] #return int.from_bytes(s, byteorder='little', signed=False)
    
    
    def get_magic_num(self, chr, power):
        """
        Return the magic check number 42 for determining if the file is
        encoded correctly.
        
        Parameters
        ----------
        chr : str
            Chromosome of interest.
        
        Return
        ------
        int
            Should return 42. If not, the file is corrupt or not being
            decoded correctly.
        """
        
        return self._get_magic_num(self._get_file(chr, power))
        
        
    def _get_bin_size(self, file):
        """
        Returns the bin size in bytes
        
        Parameters
        ----------
        file : str
            Path to bin count file.
        
        Returns
        -------
        int
            Bin size in bytes, either 1, 2, or 4.
        """
        
        s = self._read_data(file, 1, seek=BIN_SIZE_OFFSET_BYTES)
        
#        f = open(file, 'rb')
#        f.seek(BIN_SIZE_OFFSET_BYTES)
#        s = f.read(1)
#        f.close()
        
        # return in bytes
        return struct.unpack('>B', s)[0]
        
        
    def get_bin_size(self, chr, power):
        """
        Returns the bin size in bytes
        
        Parameters
        ----------
        chr : str
            Chromosome of interest.
        
        Returns
        -------
        int
            Bin size in bytes, either 1, 2, or 4.
        """
        if power not in self.bin_size_map[chr]:
            self.bin_size_map[chr][power] = self._get_bin_size(self._get_file(chr, power))
            
        return self.bin_size_map[chr][power]
    
    @property
    def reads(self):
        """
        Return the number of reads in the library.
        
        Returns
        -------
        int
            The number of reads in the library.
        """
        
        if self._reads == -1:
            # Cache the number of reads
            file = 'reads.{}.{}.bc'.format(self.genome, self.mode)
            
            if os.path.exists(file):
                f = open(file, 'rb')
                self._reads = struct.unpack('>I', f.read(4))[0]
                f.close()
        
        return self._reads
    
    def _get_bin_width(self, file):
#        f = open(file, 'rb')
#        f.seek(BIN_WIDTH_OFFSET_BYTES)
#        s = f.read(4)
#        f.close()
        
        s = self._read_data(file, 4, seek=BIN_WIDTH_OFFSET_BYTES)
        
        # return in bytes
        return struct.unpack('>I', s)[0]
    
    def get_bin_width(self, chr):
        return self._get_bin_width(self._get_file(chr))
        
    
    def _get_bin_count(self, file):
#        f = open(file, 'rb')
#        f.seek(N_BINS_OFFSET_BYTES)
#        s = f.read(4)
#        f.close()
        
        s = self._read_data(file, 4, seek=N_BINS_OFFSET_BYTES)
        
        # return in bytes
        return struct.unpack('>I', s)[0]
        
    def get_bin_count(self, chr):
        return self._get_bin_count(self._get_file(chr))
        
    
    def _get_counts(self, file, loc, bin_width, bin_size):
        sb = loc.start // bin_width
        eb = loc.end // bin_width
        n = max(1, eb - sb)
        
        sa = sb
        sn = n
        
        if bin_size > 1:
            sa *= bin_size
            sn *= bin_size
        
#        f = open(file, 'rb')
        
        # start address of seek
        
        #print('sa', BINS_OFFSET_BYTES, sa)
        
#        f.seek(BINS_OFFSET_BYTES + sa)
#        # read block of bytes to reduce file io
#        d = f.read(sn)
#        f.close()
        
        d = self._read_data(file, sn, seek=BINS_OFFSET_BYTES + sa)
        
        ret = np.zeros(n, dtype=int)
        
        if bin_size == 4:
            d_type = '>I'
        elif bin_size == 2:
            d_type = '>H'
        else:
            d_type = '>B'
            
        di = 0
        dn = len(d)
            
        for i in range(0, n):
            if di >= dn:
                break
            
            ret[i] = struct.unpack(d_type, d[di:(di + bin_size)])[0]
            di += bin_size
                
        return ret
        
    
    def get_counts(self, loc, bin_width):
        """
        Returns the counts of a binned region spanning the genomic
        coordinates.
        
        Parameters
        ----------
        loc : str or libdna.Loc
            Either a genomic coordinate of the form 'chr1:1-2' or a
            libdna.Loc object
        bin_width : int
            The size of the desired bins within the genomic coordinate.
            If bins are joined together, the average of each bin rounded to
            the nearest int is returned.
        
        Return
        ------
        list
            List of counts in each bin (ints).
        """
        
        loc = libdna.parse_loc(loc)
        
        if loc is None:
            return NO_DATA
            
#        if bin_width != BIN_WIDTH:
#            # In order to ensure that the averages are consistent as
#            # we move around, reset the loc so that the start 
#            # corresponds with the bin. To explain why consider this
#            # The stored bin width is 100. If we choose a bin width
#            # of 1000 and slide the window around a little, we may
#            # pick a start point at 700,800 etc. Since the desired
#            # bin width is 1000, we will alter which bins are used to
#            # create the average and thus as we slide the average will
#            # jump about
#            s = loc.start // bin_width * bin_width
#            e = loc.end // bin_width * bin_width
#            
#            loc = libdna.Loc(loc.chr, s, e)
        
        power = POWER[bin_width]
        
        file = self._get_file(loc.chr, power)
        
        if file is None or file == '':
            return NO_DATA
        
        bin_size = self.get_bin_size(loc.chr, power)
        
        #print(file)
        #print(self.get_magic_num(loc.chr))
        #print(bin_size)
        #print(self.get_bin_width(loc.chr))
        #print(self.get_bin_count(loc.chr))
        
        d = self._get_counts(file, loc, bin_width, bin_size)
        
        if len(d) == 0:
            return NO_DATA
                
        if bin_width < MIN_BIN_WIDTH:
            # Take averages when bins are not the same size as the
            # reference, e.g. if bin width is 1000, we take the mean
            # of the 10 bins that will fit in that bin
            
            sb = loc.start // bin_width
            eb = loc.end // bin_width
            
            i = 0
                
            # if we select a window less than BIN_WIDTH, use the BIN_WIDTH
            # window data to pad the smaller bins, thus for example if
            # BIN_WIDTH = 100 and we choose a bin size of 10, if
            # d_BIN_WIDTH[0] = 1 then d_bin[0:10] = 1 since we just 
            # duplicate the values for the 10 bins that represent 1
            # large bin. In some sense, this functionality is of little
            # practical use and is discouraged.
            f = MIN_BIN_WIDTH // bin_width
            n = max(1, eb - sb)
            
            d2 = np.zeros(n, dtype=int)
            
            for i2 in range(0, n):
                d2[i2] = d[i]
                
                if (i2 + 1) % f == 0:
                    i += 1
             
            d = d2
        
        return d
    
    
class S3BinCountReader(BinCountReader):
    def __init__(self, bucket, genome, mode='max'):
        super().__init__(bucket, genome, mode=mode)
        self.fs = s3fs.S3FileSystem(anon=True)
    
    def _get_file(self, chr, power):
        if power not in self.file_map[chr]:
            # Need to search for exact chr within file otherwise chr1 can map
            # to chr10 etc.
            s = chr + '.'
            p = '{}bw'.format(power)
            
            for file in self.fs.ls(self._dir):
                if s in file and self.genome in file and p in file and self.mode in file:
                    self.file_map[chr][power] = file #os.path.join(self.dir, file)
                    break
                
        return self.file_map[chr][power]
    
    def _read_data(self, file, n, seek=0):
        f = self.fs.open(file, 'rb')
        f.seek(seek)
        data = f.read(n)
        return data