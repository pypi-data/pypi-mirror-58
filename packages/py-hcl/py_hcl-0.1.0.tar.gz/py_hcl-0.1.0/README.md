# Py-HCL
[![Build Status](https://travis-ci.com/scutdig/py-hcl.svg?branch=master)](https://travis-ci.com/scutdig/py-hcl)
[![codecov](https://codecov.io/gh/scutdig/py-hcl/branch/master/graph/badge.svg)](https://codecov.io/gh/scutdig/py-hcl)

PyHCL is a hardware construct language like [Chisel](https://github.com/freechipsproject/chisel3) but more lightweight and more relaxed to use.
As a novel hardware construction framework embedded in Python, PyHCL supports several useful features include object-oriented, functional programming,
and dynamically typed objects.

The goal of PyHCL is providing a complete design and verification tool flow for heterogeneous computing systems flexibly using the same design methodology.

PyHCL is powered by [FIRRTL](https://github.com/freechipsproject/firrtl), an intermediate representation for digital circuit design. With the FIRRTL 
compiler framework, PyHCL-generated circuits can be compiled to the widely-used HDL Verilog.  

## 

## Getting Started

### Installing PyHCL

```shell script
$ pip install py-hcl
```