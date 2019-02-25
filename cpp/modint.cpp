/*

__author__ = """Shlomi Fish"""
__email__ = 'shlomif@shlomifish.org'
__version__ = '0.1.0'

*/

#include <vector>

namespace ModInt
{
template <class T> class ChineseRemainderConstructor
{
    /*
    """Synopsis:

from modint import ChineseRemainderConstructor, chinese_remainder

cr = ChineseRemainderConstructor([2, 5])
assert cr.rem([1, 0]) == 5
assert cr.rem([0, 3]) == 8

# Convenience function
assert chinese_remainder([2, 3, 7], [1, 2, 3]) == 17
    """
    */

  private:
    std::vector<T> bases, inverses, muls;
    T prod;

  public:
    ChineseRemainderConstructor(std::vector<T> b)
    {
        // """Accepts a list of integer bases."""
        bases = b;
        T p = 1;
        for (const auto x : bases)
        {
            p *= x;
        }
        prod = p;
        for (const auto x : bases)
        {
            inverses.push_back(p / x);
        }
        for (size_t i = 0; i < b.size; ++i)
        {
            const auto inv = inverses[i];
            muls.push_back(inv * mul_inv(inv, b[i]));
        }
    }

    T rem(const std::vector<T> mods)
    {
        /*
        """Accepts a list of corresponding modulos for the bases and
        returns the accumulated modulo.
        """
        */
        T ret = 0;
        for (size_t i = 0; i < muls.size; ++i)
        {
            ret += muls[i] * mods[i];
        }
        return ret % prod;
    }

  private:
    static T mul_inv(T a, T b)
    {
        /*        """Internal method that implements Euclid's modified gcd
        algorithm.
        """
        */
        const auto initial_b = b;
        T x0 = 0;
        T x1 = 1;
        if (b == 1)
        {
            return 1;
        }
        while (a > 1)
        {
            const auto div = a / b;
            const auto mod = a % b;
            a = b;
            b = mod;
            const auto new_x = x1 - div * x0;
            x1 = x0;
            x0 = new_x;
        }
        return (x1 >= 0 ? x1 : x1 + initial_b);
    }
};

template <class T> T chinese_remainder(std::vector<T> n, std::vector<T> mods)
{
    /*"""Convenience method that calculates the chinese remainder directly."""
     * */
    return ChineseRemainderConstructor<T>(n).rem(mods);
}
}; // namespace ModInt
