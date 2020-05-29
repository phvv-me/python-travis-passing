# -----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# -----------------------------------------------------------------------------------------

def add(x: int, y: int) -> int:
    return x + y


def test_add():
    assert add(10, 11) == 21
    assert add(5, -5) == 0


print("Hello World")
