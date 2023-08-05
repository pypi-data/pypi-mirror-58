# TODO write tests
# >>> freq = CodeList(id='CL_FREQ', names={"EN": "Frequency"}, codes=[Code(value='A', descriptions={}), Code(value='Q', descriptions={})])
# >>> country = CodeList(id='CL_COUNTRY', names={"EN": "Country"}, codes=[Code(value='FR', descriptions={}), Code(value='DE', descriptions={})])
# >>> dimensions = [
# ...     Dimension(codelist_id='CL_FREQ', concept_id='FREQ'),
# ...     Dimension(codelist_id='CL_COUNTRY', concept_id='COUNTRY'),
# ... ]
# >>> structure = Structure(codelists=[freq, country], dimensions=dimensions, names={}, concepts=[], attributes=[])
# >>> structure.dimension_mask({})
# ''
# >>> structure.dimension_mask({'FREQ': ['A'], 'COUNTRY': 'FR'})
# '.'
# >>> structure.dimension_mask([(["A", "M"], 2), (["FR", "IT"], 2)])
# '.'
# >>> structure.dimension_mask([(["A", "M"], 4), (["FR", "IT"], 10)])
# 'A+M.FR+IT'
# >>> structure.dimension_mask([(["A", "M"], 4), (["FR", "IT"], 2)])
# 'A+M.'
# >>> structure.dimension_mask([(["A", "M"], 2), (["FR", "IT"], 10)])
# '.FR+IT'
