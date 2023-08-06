o3 - reads configuration from environment variables
====================================================

The quick summary:

Ozone or trioxide, is an allotrope of Oxygen. It's found in the higher
atmosphere, and can also be smelled after rain.
Ozone configuration library is meant to be used when building cloud native
applications (or 12 Factor applications).

Usually these application are configured with environment variables. These in
turn are constants usually typed as SOME-VARIABLE. To read this in Python you
would do this::


  >>> import os
  >>> os.getenv("SHIFTSOME_VARIABLE")

I got tired of this and I want to access SOME-VARIABLE as an attribute, so::

  export SOME_VARIABLE=magic

  >>> from o3 import Config
  >>> c = Config()
  >>> c.some_variable
  magic


Notice, access is done via attribue instead of dictionary lookup.
