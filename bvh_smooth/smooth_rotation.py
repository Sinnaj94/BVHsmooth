import angle
import bvh
import freqfilter
import spacefilter


def butterworth(input_file, output_file, border=100, u0=60, order=2):
    bvh_file = bvh.read_file(input_file)

    for j in range(len(bvh_file["ROTATIONS"][0, :, 0])):
        for i in range(3):
            v = angle.floats_to_degrees(bvh_file["ROTATIONS"][:, j, i])
            p = angle.degrees_to_polars(v)
            f = freqfilter.fft(p, border)
            fil = freqfilter.butter_worth_filter(len(f), u0, order)
            f_filtered = freqfilter.apply_filter(f, fil)
            f_filtered = freqfilter.ifft(f_filtered, border)
            p = angle.complexes_to_polars(f_filtered)
            nv = angle.polars_to_degrees(p)
            bvh_file["ROTATIONS"][:, j, i] = nv

    bvh.write_file(output_file, bvh_file)


def average(input_file, output_file, m=10):
    bvh_file = bvh.read_file(input_file)

    for j in range(len(bvh_file["ROTATIONS"][0, :, 0])):
        for i in range(3):
            v = angle.floats_to_degrees(bvh_file["ROTATIONS"][:, j, i])
            p = angle.degrees_to_polars(v)
            f_filtered = spacefilter.apply_average(p, m)
            p = angle.complexes_to_polars(f_filtered)
            nv = angle.polars_to_degrees(p)
            bvh_file["ROTATIONS"][:, j, i] = nv

    bvh.write_file(output_file, bvh_file)


def gaussian(input_file, output_file, border=100, sigma=10):
    bvh_file = bvh.read_file(input_file)

    for j in range(len(bvh_file["ROTATIONS"][0, :, 0])):
        for i in range(3):
            v = angle.floats_to_degrees(bvh_file["ROTATIONS"][:, j, i])
            p = angle.degrees_to_polars(v)
            f = freqfilter.fft(p, border)
            fil = freqfilter.gaussian_filter(len(f), sigma)
            f_filtered = freqfilter.apply_filter(f, fil)
            f_filtered = freqfilter.ifft(f_filtered, border)
            p = angle.complexes_to_polars(f_filtered)
            nv = angle.polars_to_degrees(p)
            bvh_file["ROTATIONS"][:, j, i] = nv

    bvh.write_file(output_file, bvh_file)
