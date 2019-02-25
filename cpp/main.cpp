/*
 * main.cpp
 * Copyright (C) 2019 Shlomi Fish <shlomif@cpan.org>
 *
 * Distributed under terms of the MIT license.
 */

#include "modint.hpp"
#include <cassert>

int main()
{
    std::vector<long> b ={2, 5};
    std::vector<long> r ={1, 0};
    auto cr = ModInt::ChineseRemainderConstructor<long>(b);
assert(cr.rem(r) == 5);
// assert cr.rem([0, 3]) == 8
    return 0;
}
