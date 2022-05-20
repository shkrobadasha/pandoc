from panflute import Header, Strong, Str, run_filters, stringify
from sys import stderr

heads = []

def headDupl(element, _):
    if isinstance(element, Header):
        beforing = stringify(element)
        if beforing in heads:
            print("You have duplicated heading!" + beforing, file = stderr)
        else:
            heads.append(beforing)

            
def makeBold(document):
    document.replace_keyword("BOLD", Strong(Str("BOLD")))

def littleHeads(element, _):
    if isinstance(element, Header) and element.level > 2:
        return Header(Str(stringify(element).upper()), level=element.level)


if __name__ == "__main__":
    run_filters([headDupl, littleHeads], prepare=makeBold)
