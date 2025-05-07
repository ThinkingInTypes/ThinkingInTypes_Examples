---
theme: default
title: Thinking in Types
titleTemplate: '%s'
author: Bruce Eckel
aspectRatio: 16/10
lineNumbers: false
class: text-center
transition: fade-out
colorSchema: light
fonts:
  # basically the text
  sans: Robot
  # use with `font-serif` css class from UnoCSS
  serif: Robot Slab
  # for code blocks, inline code, etc.
  mono: JetBrains Mono
background: background.png
---

# Make Illegal States Unrepresentable

## Pycon 2025 Typing Summit

#### Bruce Eckel

---
layout: image
image: background.png
backgroundSize: contain
class: text-center
---


---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/string_phone_numbers.py {*}{maxHeight:'350px'}

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/phone_number_functions.py {*}{maxHeight:'350px'}

---
layout: center
---

# Design by Contract Preconditions

### (Bertrand Meyer; Eiffel Language)

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/require.py {*}{maxHeight:'340px'}

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/basic_requires.py {*}{maxHeight:'340px'}

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/bank_account.py {*}{maxHeight:'340px'}

---
zoom: 1.7
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/amount.py {*}{maxHeight:'350px'}

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/bad_amount.py

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/balance.py

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/typed_bank_account.py {*}{maxHeight:'340px'}

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/phone_number.py {*}{maxHeight:'340px'}

---
zoom: 1.8
layout: full
class: pl-3 pr-0 max-w-none w-full py-0
---
<<< @/../c11_make_illegal_types_unrepresentable/phone_numbers_as_types.py {*}{maxHeight:'340px'}

---
layout: image-left
image: background.png
backgroundSize: contain
class: text-center
---

# Questions...
