import warnings
import iso3166

# fuzzywuzzy warns that we haven't installed the C module.
# suppress and ignore.
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from fuzzywuzzy import process

country_codes = [c.alpha3 for c in iso3166.countries]

def is_valid_iso_cc(code):
    """Is ``code`` a valid ISO-3166 code?

    :param code: country code to validate
    :type code: str
    :rtype: (bool, list)
    :returns: (True, []) if code is valid, (False, [matches]) otherwise

    .. versionadded:: 0.3.0
        Fuzzy matches returned on no match.

    .. code-block:: python

        from poplar_isocc import is_valid_iso_cc

        # Check if a code is valid.
        is_valid_iso_cc("CA")
            # returns True
        is_valid_iso_cc("ZZ")
            # returns False
    """
    if not code in country_codes:
        fuzzy_matches = process.extract(code, country_codes, limit=3)
        return False, [fm[0] for fm in fuzzy_matches]
    return True, []
