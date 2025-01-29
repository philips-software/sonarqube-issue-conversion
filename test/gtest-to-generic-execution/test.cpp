#include <gmock/gmock.h>
#include <gtest/gtest.h>

TEST(Test, should_calculate)
{
    EXPECT_THAT(1 + 1, testing::Eq(2));
}
