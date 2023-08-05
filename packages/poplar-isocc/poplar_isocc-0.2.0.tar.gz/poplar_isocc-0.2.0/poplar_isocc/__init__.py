import iso3166

country_codes = [c.alpha3 for c in iso3166.countries]

def is_valid_iso_cc(code):
    """Is ``code`` a valid ISO-3166 code?

    :param code: country code to validate
    :type code: str
    :rtype: bool
    :returns: True if code is valid.

    .. code-block:: python

        from poplar_isocc import is_valid_iso_cc

        # Check if a code is valid.
        is_valid_iso_cc("CA")
            # returns True
        is_valid_iso_cc("ZZ")
            # returns False
    """
    return code in country_codes
