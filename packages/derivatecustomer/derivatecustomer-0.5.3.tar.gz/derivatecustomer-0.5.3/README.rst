================
DerivateCustomer
================

AgriConnect internal tool to make a derivation of PlantingHouse for customer.

Usage
-----

- Fork the PlantingHouse repo.
- Go to "Settings > General > Change path", change to customer codename.
- Run the command, passing forked repo URL. Example:

.. code-block:: sh

    python3 -m derivatecustomer -g git@gitlab.com:quan/phuc-daothanh.git -n "Phúc Đạo Thạnh" -s fa
