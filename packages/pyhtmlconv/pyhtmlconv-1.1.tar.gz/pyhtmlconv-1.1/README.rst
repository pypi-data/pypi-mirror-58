pyhtmlconv: html converter (image / pdf)
----------------------------------------

python html converter (image / pdf)

Installation
------------

Anda perlu menginstall `wkhtmltopdf <https://wkhtmltopdf.org/>`_, sebelum menginstall modul ini.

.. code-block:: bash

    pip install pyhtmlconv

Example
-------

.. code-block:: python

    import pyhtmlconv as html
    url = "https://google.com"
    image = html.convert_to_image(url, "jpeg")
    with open("test_image.jpeg", "wb") as fp:
        fp.write(image)

    pdf = html.convert_to_pdf(url)
    with open("test_file.pdf") as fp:
        fp.write(pdf)

Anda juga dapat mengkonversikan data (image atau pdf) ke bentuk `data uri <https://tools.ietf.org/html/rfc2397>`_ dengan cara menambahkan nilai ``True`` pada parameter ``datauri`` di fungsi ``convert_to_image`` atau ``convert_to_pdf``.
