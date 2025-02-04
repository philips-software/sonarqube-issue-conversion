#include <gmock/gmock.h>
#include <gtest/gtest.h>

TEST(CalculatorTest, should_add_two_numbers)
{
    EXPECT_THAT(1 + 1, testing::Eq(2));
}
