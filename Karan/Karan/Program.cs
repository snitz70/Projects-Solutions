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
    }
}
