using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Karan
{
    class Program
    {
        static void Main(string[] args)
        {
        }
    }

    public static class Numbers
    {
        public static double CalculatePi(int decimalPlaces)
        {

            return System.Math.Round(System.Math.PI, decimalPlaces);
        }

        public static double CalculateE(int decimalPlaces)
        {
            return System.Math.Round(System.Math.E, decimalPlaces);
        }

        public static int[] Fibonacci(int number)
        {
            int[] fib = new int[number];
            fib[0] = fib[1] = 1;
            for(int i=2; i<number; ++i)
            {
                fib[i] = fib[i - 1] + fib[i - 2];
            }
            return fib;


        }
    }
}
