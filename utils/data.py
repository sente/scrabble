
def uniq_stable(elems):
    # http://ipython.scipy.org/doc/manual/html/api/generated/IPython.utils.data.html
    """uniq_stable(elems) -> list

    Return from an iterable, a list of all the unique elements in the input,
    but maintaining the order in which they first appear.

    A naive solution to this problem which just makes a dictionary with the
    elements as keys fails to respect the stability condition, since
    dictionaries are unsorted by nature.

    Note: All elements in the input must be valid dictionary keys for this
    routine to work, as it internally uses a dictionary for efficiency
    reasons."""

    unique = []
    unique_dict = {}
    for nn in elems:
        if nn not in unique_dict:
            unique.append(nn)
            unique_dict[nn] = None
    return unique

def uniq(elems):
    return uniq_stable(elems)
