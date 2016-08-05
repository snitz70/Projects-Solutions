using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Linq;
using Karan;

namespace karan.UnitTests
{
    [TestClass]
    public class FindPiTest
    {
        [TestMethod]
        public void FindPiTwoDecimalPlaces()
        {
            double expectedResult = 3.14;
            double actualResult = Karan.Numbers.CalculatePi(2);
            Assert.AreEqual(expectedResult, actualResult);
        }

        [TestMethod]
        public void FindPiFiveDecimalPlaces()
        {
            double expectedResult = 3.14159;
            double actualResult = Karan.Numbers.CalculatePi(5);
            Assert.AreEqual(expectedResult, actualResult);
        }
    }

    [TestClass]
    public class FindeTest
    {
        [TestMethod]
        public void FindEToFiveDecimalPlaces()
        {
            double expectedResult = 2.71828;
            double actualResult = Karan.Numbers.CalculateE(5);
        }
    }

    [TestClass]
    public class Fibonacci
    {
        [TestMethod]
        public void CalculateFibonacci()
        {
            int[] expectedResult = { 1, 1, 2, 3, 5, 8, 13 };
            int[] actualResult = Karan.Numbers.Fibonacci(7);
            bool isEqual = expectedResult.SequenceEqual(actualResult);
            Assert.IsTrue(isEqual);
            

        }
    }


}
