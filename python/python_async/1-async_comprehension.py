#!/usr/bin/env python3
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ comprehesion = []
    async for i in async_generator():
        comprehesion.append(i)
    return comprehesion """
    
    return [element async for element in async_generator()]
