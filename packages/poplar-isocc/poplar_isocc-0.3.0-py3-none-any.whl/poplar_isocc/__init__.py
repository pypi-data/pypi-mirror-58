import iso3166
import fuzzywuzzy

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
    if not code in country_codes:
        fuzzy_matches = fuzzywuzzy.process(code, country_codes, limit=3)
        return False, [fm[0] for fm in fuzzy_matches]
    return True, []
