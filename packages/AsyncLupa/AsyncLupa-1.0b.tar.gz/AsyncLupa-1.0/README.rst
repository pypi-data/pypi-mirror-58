AsyncLupa
=========

AsyncLupa integrates with the well known Lupa_ library, providing an asynchronous wrapper allowing
async function / method calls right from Lua.

.. _Lupa: https://github.com/scoder/lupa

Installation
------------
.. code-block::

    pip install AsyncLupa

If you want the latest version that has not yet been released

.. code-block::

    pip install git+https://github.com/SoulSen/AsyncLupa

Calling Async functions in Lua
------------------------------
AsyncLupa support all Lupa's methods that execute Lua code in any way.
It includes ``AsyncLupa.execute``, ``AsyncLupa.eval``, and ``AsyncLupa.compile``, it also supports all the other methods also.

An example is shown below

.. code-block:: python

    from asynclupa import AsyncLuaRuntime
    import asyncio

    async def hello():
        return 1

    async def main():
        async_lua = AsyncLuaRuntime()
        async_lua.globals()['hello'] = hello

        ret = await async_lua.eval('return python.coroutine(hello())')
        print(ret)  # Outputs 1

    asyncio.run(eval_lua(lua_code))


