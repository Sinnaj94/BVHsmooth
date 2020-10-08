import numpy as np
import bvh
import freqfilter
import spacefilter


def butterworth(input_file, output_file, border=100, u0=60, order=2):
    bvh_file = bvh.read_file(input_file)

    for i in range(0, 3):
        v = bvh_file["POSITIONS"][:, i]
        f = freqfilter.fft(v, border)
        fil = freqfilter.butter_worth_filter(len(f), u0, order)
        ff = freqfilter.apply_filter(f, fil)
        iff = freqfilter.ifft(ff, border)
        bvh_file["POSITIONS"][:, i] = np.real(iff)

    bvh.write_file(output_file, bvh_file)


def average(input_file, output_file, m=10):
    bvh_file = bvh.read_file(input_file)

    for i in range(0, 3):
        v = bvh_file["POSITIONS"][:, i]
        bvh_file["POSITIONS"][:, i] = spacefilter.apply_average(v, m)

    bvh.write_file(output_file, bvh_file)


def gaussian(input_file, output_file, border=100, sigma=10):
    bvh_file = bvh.read_file(input_file)

    for i in range(0, 3):
        v = bvh_file["POSITIONS"][:, i]
        f = freqfilter.fft(v, border)
        fil = freqfilter.gaussian_filter(len(f), sigma)
        ff = freqfilter.apply_filter(f, fil)
        iff = freqfilter.ifft(ff, border)
        bvh_file["POSITIONS"][:, i] = np.real(iff)

    bvh.write_file(output_file, bvh_file)
