#!/usr/bin/env python3
import re

regexp = "(?:\\{\\s*1:(.+?)\\})?\\s*(?:\\{\\s*2:(.+?)\\})?\\s*(?:\\{\\s*3:(.+?)\\}(?=\\s*\\{))?\\s*\\{\\s*4:(.+?)-\\}" \
        "(?:\\s*\\{\\s*5:((?:\\{.+?\\})+)\\})?"


regexp2 = "(?:\\{\\s*1:(.+?)\\})?\\s*(?:\\{\\s*2:(.+?)\\})?\\s*(?:\\{\\s*3:(.+?)\\}(?=\\s*\\{))?\\s*\\" \
          "{\\s*4:(.+?)-\\}" \
          "(?:\\s*\\{\\s*5:((?:\\{.+?\\})+)\\})?"



def is_match(exp, new_regexp, print_res=True):

    p = re.compile(new_regexp, flags=re.IGNORECASE)

    match = p.match(exp)
    if match:
        match_text = match.group()
        if print_res:
            print("Found a match for ", exp, " --> ", match_text)
    else:
        if print_res:
            print("No match for ", exp)
        return False
    return match.group()


is_match("{4::20:DZ -}", regexp)
is_match("{4::20:DZ -", regexp)
is_match("{4::20:DZ }", regexp)
is_match("4::20:DZ -}", regexp)













