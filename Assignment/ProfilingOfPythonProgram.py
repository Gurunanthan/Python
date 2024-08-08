import cProfile
import pstats
import io
def sample_function():
    total = 0
    for i in range(10000):
        total += i
    return total
def main():
    profiler = cProfile.Profile()
    profiler.enable()
    sample_function()
    profiler.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
if __name__ == "__main__":
    main()
