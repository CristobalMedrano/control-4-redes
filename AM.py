from numpy import sin, cos, pi, arange, fft
import matplotlib.pyplot as plt

def signal(t):
    return cos(2*pi*3*t) + sin(2*pi*2*t)

def carrier_signal(fs, t):
    return cos((2*pi*fs)*t)

def plot_signal(t, f, title, xlabel, ylabel, left_lim, right_lim):
    plt.figure(title)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(t, f)
    plt.xlim(left_lim, right_lim)
    plt.grid()

def main():
    t = arange(0, 1, 0.001)
    f = signal(t)

    f_wave_fft = abs(fft.fft(f))
    f_fs_fft = fft.fftfreq(f_wave_fft.size) 
    
    plot_signal(t, f, "Signal in time", "time (s)", "amplitude", 0, 0.1)
    plot_signal(f_fs_fft, f_wave_fft, "Signal in frequency", "frequency (hz)", "|f(w)|", -0.3, 0.3)

    f_carrier = carrier_signal(100, t)
    f_carrier_wave_fft = abs(fft.fft(f_carrier))
    f_carrier_fs_fft = fft.fftfreq(f_carrier_wave_fft.size) 
    
    plot_signal(t, f_carrier, "Carrier Signal in time", "time (s)", "amplitude", 0, 0.1)
    plot_signal(f_carrier_fs_fft, f_carrier_wave_fft, "Carrier Signal in frequency", "frequency (hz)", "|f(w)|", -0.3, 0.3)

    f_modulated = f*f_carrier
    f_modulated_wave_fft = abs(fft.fft(f_modulated))
    f_modulated_fs_fft = fft.fftfreq(f_modulated_wave_fft.size) 
    plot_signal(t, f_modulated, "Signal Modulated in time", "time (s)", "amplitude", 0, 0.1)
    plot_signal(f_modulated_fs_fft, f_modulated_wave_fft, "Signal Modulated in frequency", "frequency (hz)", "|f(w)|", -0.3, 0.3)
    plt.show()

    return 0

main()