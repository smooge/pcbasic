
# Codepage 437 to Unicode table 
# with Special Graphic Characters
# http://en.wikipedia.org/wiki/Code_page_437
# http://msdn.microsoft.com/en-us/library/cc195060.aspx
# http://msdn.microsoft.com/en-us/goglobal/cc305160

import sys

def from_unicode(s):
    output = ''
    for c in s:
        if ord(c) == 0:
            # double NUL characters as single NUL signals scan code
            output += '\x00\x00'
        else:
            try: 
                output += chr(unicode_to_cp[c])
            except KeyError:
                if ord(c) <= 0xff:
                    output += chr(ord(c))
    return output

def load_codepage(number=437):
    global cp_to_unicode, unicode_to_cp, cp_to_utf8, utf8_to_cp
    try:
        cp_to_unicode = codepage[number]
    except KeyError:
        sys.stderr.write('WARNING: Could not find unicode table for codepage %d. Falling back to codepage 437 (US).\n' % number)
        cp_to_unicode = codepage[437]
    cp_to_unicode.update(ascii)    
    cp_to_unicode.update(special_graphic)    
    unicode_to_cp = dict((reversed(item) for item in cp_to_unicode.items()))
    cp_to_utf8 = dict([ (chr(s[0]), s[1].encode('utf-8')) for s in cp_to_unicode.items()])
    utf8_to_cp = dict((reversed(item) for item in cp_to_utf8.items()))
      
      
ascii = dict(( (c, unichr(c)) for c in range(127) ))

special_graphic = {
    0x00:   u'\u0000',     0x01:   u'\u263A',      0x02:   u'\u263B',     0x03:   u'\u2665',      0x04:   u'\u2666',    
    0x05:   u'\u2663',     0x06:   u'\u2660',      0x07:   u'\u2022',     0x08:   u'\u25D8',      0x09:   u'\u25CB',      
    0x0a:   u'\u25D9',     0x0b:   u'\u2642',      0x0c:   u'\u2640',     0x0d:   u'\u266A',      0x0e:   u'\u266B',      
    0x0f:   u'\u263C',     0x10:   u'\u25BA',      0x11:   u'\u25C4',     0x12:   u'\u2195',      0x13:   u'\u203C',      
    0x14:   u'\u00B6',     0x15:   u'\u00A7',      0x16:   u'\u25AC',     0x17:   u'\u21A8',      0x18:   u'\u2191',      
    0x19:   u'\u2193',     0x1a:   u'\u2192',      0x1b:   u'\u2190',     0x1c:   u'\u221F',      0x1d:   u'\u2194',     
    0x1e:   u'\u25B2',     0x1f:   u'\u25BC',      0x7f:   u'\u2302',
    }        

codepage = {
    775 :  { 128: u'\u0106', 129: u'\xfc', 130: u'\xe9', 131: u'\u0101', 132: u'\xe4', 133: u'\u0123', 134: u'\xe5', 135: u'\u0107', 
             136: u'\u0142', 137: u'\u0113', 138: u'\u0156', 139: u'\u0157', 140: u'\u012b', 141: u'\u0179', 142: u'\xc4', 143: u'\xc5',
             144: u'\xc9', 145: u'\xe6', 146: u'\xc6', 147: u'\u014d', 148: u'\xf6', 149: u'\u0122', 150: u'\xa2', 151: u'\u015a', 
             152: u'\u015b', 153: u'\xd6', 154: u'\xdc', 155: u'\xf8', 156: u'\xa3', 157: u'\xd8', 158: u'\xd7', 159: u'\xa4', 
             160: u'\u0100', 161: u'\u012a', 162: u'\xf3', 163: u'\u017b', 164: u'\u017c', 165: u'\u017a', 166: u'\u201d', 167: u'\xa6',
             168: u'\xa9', 169: u'\xae', 170: u'\xac', 171: u'\xbd', 172: u'\xbc', 173: u'\u0141', 174: u'\xab', 175: u'\xbb', 
             176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\u0104', 182: u'\u010c', 
             183: u'\u0118', 184: u'\u0116', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\u012e', 
             190: u'\u0160', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 
             197: u'\u253c', 198: u'\u0172', 199: u'\u016a', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566',
             204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\u017d', 208: u'\u0105', 209: u'\u010d', 210: u'\u0119', 
             211: u'\u0117', 212: u'\u012f', 213: u'\u0161', 214: u'\u0173', 215: u'\u016b', 216: u'\u017e', 217: u'\u2518', 
             218: u'\u250c', 219: u'\u2588', 220: u'\u2584', 221: u'\u258c', 222: u'\u2590', 223: u'\u2580', 224: u'\xd3', 
             225: u'\xdf', 226: u'\u014c', 227: u'\u0143', 228: u'\xf5', 229: u'\xd5', 230: u'\xb5', 231: u'\u0144', 232: u'\u0136',
             233: u'\u0137', 234: u'\u013b', 235: u'\u013c', 236: u'\u0146', 237: u'\u0112', 238: u'\u0145', 239: u'\u2019', 
             240: u'\xad', 241: u'\xb1', 242: u'\u201c', 243: u'\xbe', 244: u'\xb6', 245: u'\xa7', 246: u'\xf7', 247: u'\u201e', 
             248: u'\xb0', 249: u'\u2219', 250: u'\xb7', 251: u'\xb9', 252: u'\xb3', 253: u'\xb2', 254: u'\u25a0', 255: u'\xa0'
             } ,
    720 :  { 130: u'\xe9', 131: u'\xe2', 133: u'\xe0', 135: u'\xe7', 136: u'\xea', 137: u'\xeb', 138: u'\xe8', 139: u'\xef', 
             140: u'\xee', 145: u'\u0651', 146: u'\u0652', 147: u'\xf4', 148: u'\xa4', 149: u'\u0640', 150: u'\xfb', 151: u'\xf9', 
             152: u'\u0621', 153: u'\u0622', 154: u'\u0623', 155: u'\u0624', 156: u'\xa3', 157: u'\u0625', 158: u'\u0626', 
             159: u'\u0627', 160: u'\u0628', 161: u'\u0629', 162: u'\u062a', 163: u'\u062b', 164: u'\u062c', 165: u'\u062d', 
             166: u'\u062e', 167: u'\u062f', 168: u'\u0630', 169: u'\u0631', 170: u'\u0632', 171: u'\u0633', 172: u'\u0634', 
             173: u'\u0635', 174: u'\xab', 175: u'\xbb', 176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524',
             181: u'\u2561', 182: u'\u2562', 183: u'\u2556', 184: u'\u2555', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 
             188: u'\u255d', 189: u'\u255c', 190: u'\u255b', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 
             195: u'\u251c', 196: u'\u2500', 197: u'\u253c', 198: u'\u255e', 199: u'\u255f', 200: u'\u255a', 201: u'\u2554', 
             202: u'\u2569', 203: u'\u2566', 204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\u2567', 208: u'\u2568', 
             209: u'\u2564', 210: u'\u2565', 211: u'\u2559', 212: u'\u2558', 213: u'\u2552', 214: u'\u2553', 215: u'\u256b', 
             216: u'\u256a', 217: u'\u2518', 218: u'\u250c', 219: u'\u2588', 220: u'\u2584', 221: u'\u258c', 222: u'\u2590', 
             223: u'\u2580', 224: u'\u0636', 225: u'\u0637', 226: u'\u0638', 227: u'\u0639', 228: u'\u063a', 229: u'\u0641', 
             230: u'\xb5', 231: u'\u0642', 232: u'\u0643', 233: u'\u0644', 234: u'\u0645', 235: u'\u0646', 236: u'\u0647', 
             237: u'\u0648', 238: u'\u0649', 239: u'\u064a', 240: u'\u2261', 241: u'\u064b', 242: u'\u064c', 243: u'\u064d', 
             244: u'\u064e', 245: u'\u064f', 246: u'\u0650', 247: u'\u2248', 248: u'\xb0', 249: u'\u2219', 250: u'\xb7', 251: u'\u221a', 
             252: u'\u207f', 253: u'\xb2', 254: u'\u25a0', 255: u'\xa0'
             } ,
    850 :  { 128: u'\xc7', 129: u'\xfc', 130: u'\xe9', 131: u'\xe2', 132: u'\xe4', 133: u'\xe0', 134: u'\xe5', 135: u'\xe7', 
             136: u'\xea', 137: u'\xeb', 138: u'\xe8', 139: u'\xef', 140: u'\xee', 141: u'\xec', 142: u'\xc4', 143: u'\xc5', 
             144: u'\xc9', 145: u'\xe6', 146: u'\xc6', 147: u'\xf4', 148: u'\xf6', 149: u'\xf2', 150: u'\xfb', 151: u'\xf9', 
             152: u'\xff', 153: u'\xd6', 154: u'\xdc', 155: u'\xf8', 156: u'\xa3', 157: u'\xd8', 158: u'\xd7', 159: u'\u0192', 
             160: u'\xe1', 161: u'\xed', 162: u'\xf3', 163: u'\xfa', 164: u'\xf1', 165: u'\xd1', 166: u'\xaa', 167: u'\xba', 
             168: u'\xbf', 169: u'\xae', 170: u'\xac', 171: u'\xbd', 172: u'\xbc', 173: u'\xa1', 174: u'\xab', 175: u'\xbb', 
             176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\xc1', 182: u'\xc2', 
             183: u'\xc0', 184: u'\xa9', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d',     189: u'\xa2', 
             190: u'\xa5', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 
             197: u'\u253c', 198: u'\xe3', 199: u'\xc3', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 
             204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\xa4', 208: u'\xf0', 209: u'\xd0', 210: u'\xca', 211: u'\xcb', 
             212: u'\xc8', 213: u'\u0131', 214: u'\xcd', 215: u'\xce', 216: u'\xcf', 217: u'\u2518', 218: u'\u250c', 219: u'\u2588', 
             220: u'\u2584', 221: u'\xa6', 222: u'\xcc', 223: u'\u2580', 224: u'\xd3', 225: u'\xdf', 226: u'\xd4', 227: u'\xd2', 
             228: u'\xf5', 229: u'\xd5', 230: u'\xb5', 231: u'\xfe', 232: u'\xde', 233: u'\xda', 234: u'\xdb', 235: u'\xd9', 
             236: u'\xfd', 237: u'\xdd', 238: u'\xaf', 239: u'\xb4', 240: u'\xad', 241: u'\xb1', 242: u'\u2017', 243: u'\xbe', 
             244: u'\xb6', 245: u'\xa7', 246: u'\xf7', 247: u'\xb8', 248: u'\xb0', 249: u'\xa8', 250: u'\xb7', 251: u'\xb9', 
             252: u'\xb3', 253: u'\xb2', 254: u'\u25a0', 255: u'\xa0'
             } ,
    852 :  { 128: u'\xc7', 129: u'\xfc', 130: u'\xe9', 131: u'\xe2', 132: u'\xe4', 133: u'\u016f', 134: u'\u0107', 135: u'\xe7', 
             136: u'\u0142', 137: u'\xeb', 138: u'\u0150', 139: u'\u0151', 140: u'\xee', 141: u'\u0179', 142: u'\xc4', 
             143: u'\u0106', 144: u'\xc9', 145: u'\u0139', 146: u'\u013a', 147: u'\xf4', 148: u'\xf6', 149: u'\u013d', 
             150: u'\u013e', 151: u'\u015a', 152: u'\u015b', 153: u'\xd6', 154: u'\xdc', 155: u'\u0164', 156: u'\u0165', 
             157: u'\u0141', 158: u'\xd7', 159: u'\u010d', 160: u'\xe1', 161: u'\xed', 162: u'\xf3', 163: u'\xfa', 164: u'\u0104', 
             165: u'\u0105', 166: u'\u017d', 167: u'\u017e', 168: u'\u0118', 169: u'\u0119', 170: u'\xac', 171: u'\u017a', 
             172: u'\u010c', 173: u'\u015f', 174: u'\xab', 175: u'\xbb', 176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 
             179: u'\u2502', 180: u'\u2524', 181: u'\xc1', 182: u'\xc2', 183: u'\u011a', 184: u'\u015e', 185: u'\u2563', 
             186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\u017b', 190: u'\u017c', 191: u'\u2510', 192: u'\u2514', 
             193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 197: u'\u253c', 198: u'\u0102', 199: u'\u0103', 
             200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 
             207: u'\xa4', 208: u'\u0111', 209: u'\u0110', 210: u'\u010e', 211: u'\xcb', 212: u'\u010f', 213: u'\u0147', 
             214: u'\xcd', 215: u'\xce', 216: u'\u011b', 217: u'\u2518', 218: u'\u250c', 219: u'\u2588', 220: u'\u2584', 
             221: u'\u0162', 222: u'\u016e', 223: u'\u2580', 224: u'\xd3', 225: u'\xdf', 226: u'\xd4', 227: u'\u0143', 
             228: u'\u0144', 229: u'\u0148', 230: u'\u0160', 231: u'\u0161', 232: u'\u0154', 233: u'\xda', 234: u'\u0155', 
             235: u'\u0170', 236: u'\xfd', 237: u'\xdd', 238: u'\u0163', 239: u'\xb4', 240: u'\xad', 241: u'\u02dd', 242: u'\u02db', 
             243: u'\u02c7', 244: u'\u02d8', 245: u'\xa7', 246: u'\xf7', 247: u'\xb8', 248: u'\xb0', 249: u'\xa8', 250: u'\u02d9', 
             251: u'\u0171', 252: u'\u0158', 253: u'\u0159', 254: u'\u25a0', 255: u'\xa0'
             } ,
    855 :  { 128: u'\u0452', 129: u'\u0402', 130: u'\u0453', 131: u'\u0403', 132: u'\u0451', 133: u'\u0401', 134: u'\u0454', 
             135: u'\u0404', 136: u'\u0455', 137: u'\u0405', 138: u'\u0456', 139: u'\u0406', 140: u'\u0457', 141: u'\u0407', 
             142: u'\u0458', 143: u'\u0408', 144: u'\u0459', 145: u'\u0409', 146: u'\u045a', 147: u'\u040a', 148: u'\u045b', 
             149: u'\u040b', 150: u'\u045c', 151: u'\u040c', 152: u'\u045e', 153: u'\u040e', 154: u'\u045f', 155: u'\u040f', 
             156: u'\u044e', 157: u'\u042e', 158: u'\u044a', 159: u'\u042a', 160: u'\u0430', 161: u'\u0410', 162: u'\u0431', 
             163: u'\u0411', 164: u'\u0446', 165: u'\u0426', 166: u'\u0434', 167: u'\u0414', 168: u'\u0435', 169: u'\u0415', 
             170: u'\u0444', 171: u'\u0424', 172: u'\u0433', 173: u'\u0413', 174: u'\xab', 175: u'\xbb', 176: u'\u2591', 
             177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\u0445', 182: u'\u0425', 183: u'\u0438', 
             184: u'\u0418', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\u0439', 190: u'\u0419', 
             191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 197: u'\u253c', 
             198: u'\u043a', 199: u'\u041a', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 204: u'\u2560', 
             205: u'\u2550', 206: u'\u256c', 207: u'\xa4', 208: u'\u043b', 209: u'\u041b', 210: u'\u043c', 211: u'\u041c', 
             212: u'\u043d', 213: u'\u041d', 214: u'\u043e', 215: u'\u041e', 216: u'\u043f', 217: u'\u2518', 218: u'\u250c', 
             219: u'\u2588', 220: u'\u2584', 221: u'\u041f', 222: u'\u044f', 223: u'\u2580', 224: u'\u042f', 225: u'\u0440', 
             226: u'\u0420', 227: u'\u0441', 228: u'\u0421', 229: u'\u0442', 230: u'\u0422', 231: u'\u0443', 232: u'\u0423', 
             233: u'\u0436', 234: u'\u0416', 235: u'\u0432', 236: u'\u0412', 237: u'\u044c', 238: u'\u042c', 239: u'\u2116', 
             240: u'\xad', 241: u'\u044b', 242: u'\u042b', 243: u'\u0437', 244: u'\u0417', 245: u'\u0448', 246: u'\u0428', 
             247: u'\u044d', 248: u'\u042d', 249: u'\u0449', 250: u'\u0429', 251: u'\u0447', 252: u'\u0427', 253: u'\xa7', 
             254: u'\u25a0', 255: u'\xa0'
             } ,
    856 :  { 128: u'\u0410', 129: u'\u0411', 130: u'\u0412', 131: u'\u0413', 132: u'\u0414', 133: u'\u0415', 134: u'\u0416', 
             135: u'\u0417', 136: u'\u0418', 137: u'\u0419', 138: u'\u041a', 139: u'\u041b', 140: u'\u041c', 141: u'\u041d', 
             142: u'\u041e', 143: u'\u041f', 144: u'\u0420', 145: u'\u0421', 146: u'\u0422', 147: u'\u0423', 148: u'\u0424', 
             149: u'\u0425', 150: u'\u0426', 151: u'\u0427', 152: u'\u0428', 153: u'\u0429', 154: u'\u042a', 155: u'\u042b', 
             156: u'\u042c', 157: u'\u042d', 158: u'\u042e', 159: u'\u042f', 160: u'\u0430', 161: u'\u0431', 162: u'\u0432', 
             163: u'\u0433', 164: u'\u0434', 165: u'\u0435', 166: u'\u0436', 167: u'\u0437', 168: u'\u0438', 169: u'\u0439', 
             170: u'\u043a', 171: u'\u043b', 172: u'\u043c', 173: u'\u043d', 174: u'\u043e', 175: u'\u043f', 176: u'\u2591', 
             177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\u2561', 182: u'\u2562', 183: u'\u2556', 
             184: u'\u2555', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\u255c', 190: u'\u255b', 
             191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 197: u'\u253c', 
             198: u'\u255e', 199: u'\u255f', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 204: u'\u2560', 
             205: u'\u2550', 206: u'\u256c', 207: u'\u2567', 208: u'\u2568', 209: u'\u2564', 210: u'\u2565', 211: u'\u2559', 
             212: u'\u2558', 213: u'\u2552', 214: u'\u2553', 215: u'\u256b', 216: u'\u256a', 217: u'\u2518', 218: u'\u250c', 
             219: u'\u2588', 220: u'\u2584', 221: u'\u258c', 222: u'\u2590', 223: u'\u2580', 224: u'\u0440', 225: u'\u0441', 
             226: u'\u0442', 227: u'\u0443', 228: u'\u0444', 229: u'\u0445', 230: u'\u0446', 231: u'\u0447', 232: u'\u0448', 
             233: u'\u0449', 234: u'\u044a', 235: u'\u044b', 236: u'\u044c', 237: u'\u044d', 238: u'\u044e', 239: u'\u044f', 
             240: u'\u0401', 241: u'\u0451', 242: u'\u0404', 243: u'\u0454', 244: u'\u0407', 245: u'\u0457', 246: u'\u040e', 
             247: u'\u045e', 248: u'\xb0', 249: u'\u2219', 250: u'\xb7', 251: u'\u221a', 252: u'\u2116', 253: u'\xa4', 
             254: u'\u25a0', 255: u'\xa0'
             } ,
    857 :  { 128: u'\xc7', 129: u'\xfc', 130: u'\xe9', 131: u'\xe2', 132: u'\xe4', 133: u'\xe0', 134: u'\xe5', 135: u'\xe7', 
             136: u'\xea', 137: u'\xeb', 138: u'\xe8', 139: u'\xef', 140: u'\xee', 141: u'\u0131', 142: u'\xc4', 143: u'\xc5',
             144: u'\xc9', 145: u'\xe6', 146: u'\xc6', 147: u'\xf4', 148: u'\xf6', 149: u'\xf2', 150: u'\xfb', 151: u'\xf9', 
             152: u'\u0130', 153: u'\xd6', 154: u'\xdc', 155: u'\xf8', 156: u'\xa3', 157: u'\xd8', 158: u'\u015e', 159: u'\u015f', 
             160: u'\xe1', 161: u'\xed', 162: u'\xf3', 163: u'\xfa', 164: u'\xf1', 165: u'\xd1', 166: u'\u011e', 167: u'\u011f', 
             168: u'\xbf', 169: u'\xae', 170: u'\xac', 171: u'\xbd', 172: u'\xbc', 173: u'\xa1', 174: u'\xab', 175: u'\xbb', 
             176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\xc1', 182: u'\xc2', 
             183: u'\xc0', 184: u'\xa9', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\xa2', 
             190: u'\xa5', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 
             197: u'\u253c', 198: u'\xe3', 199: u'\xc3', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 
             204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\xa4', 208: u'\xba', 209: u'\xaa', 210: u'\xca', 211: u'\xcb', 
             212: u'\xc8', 214: u'\xcd', 215: u'\xce', 216: u'\xcf', 217: u'\u2518', 218: u'\u250c', 219: u'\u2588', 220: u'\u2584', 
             221: u'\xa6', 222: u'\xcc', 223: u'\u2580', 224: u'\xd3', 225: u'\xdf', 226: u'\xd4', 227: u'\xd2', 228: u'\xf5', 
             229: u'\xd5', 230: u'\xb5', 232: u'\xd7', 233: u'\xda', 234: u'\xdb', 235: u'\xd9', 236: u'\xec', 237: u'\xff', 
             238: u'\xaf', 239: u'\xb4', 240: u'\xad', 241: u'\xb1', 243: u'\xbe', 244: u'\xb6', 245: u'\xa7', 246: u'\xf7', 
             247: u'\xb8', 248: u'\xb0', 249: u'\xa8', 250: u'\xb7', 251: u'\xb9', 252: u'\xb3', 253: u'\xb2', 254: u'\u25a0', 
             255: u'\xa0'
             } ,
    858 :  { 128: u'\xc7', 129: u'\xfc', 130: u'\xe9', 131: u'\xe2', 132: u'\xe4', 133: u'\xe0', 134: u'\xe5', 135: u'\xe7', 
             136: u'\xea', 137: u'\xeb', 138: u'\xe8', 139: u'\xef', 140: u'\xee', 141: u'\xec', 142: u'\xc4', 143: u'\xc5', 
             144: u'\xc9', 145: u'\xe6', 146: u'\xc6', 147: u'\xf4', 148: u'\xf6', 149: u'\xf2', 150: u'\xfb', 151: u'\xf9', 
             152: u'\xff', 153: u'\xd6', 154: u'\xdc', 155: u'\xf8', 156: u'\xa3', 157: u'\xd8', 158: u'\xd7', 159: u'\u0192', 
             160: u'\xe1', 161: u'\xed', 162: u'\xf3', 163: u'\xfa', 164: u'\xf1', 165: u'\xd1', 166: u'\xaa', 167: u'\xba', 
             168: u'\xbf', 169: u'\xae', 170: u'\xac', 171: u'\xbd', 172: u'\xbc', 173: u'\xa1', 174: u'\xab', 175: u'\xbb', 
             176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\xc1', 182: u'\xc2', 
             183: u'\xc0', 184: u'\xa9', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\xa2', 
             190: u'\xa5', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 
             197: u'\u253c', 198: u'\xe3', 199: u'\xc3', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 
             204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\xa4', 208: u'\xf0', 209: u'\xd0', 210: u'\xca', 211: u'\xcb', 
             212: u'\xc8', 213: u'\u20ac', 214: u'\xcd', 215: u'\xce', 216: u'\xcf', 217: u'\u2518', 218: u'\u250c', 219: u'\u2588', 
             220: u'\u2584', 221: u'\xa6', 222: u'\xcc', 223: u'\u2580', 224: u'\xd3', 225: u'\xdf', 226: u'\xd4', 227: u'\xd2', 
             228: u'\xf5', 229: u'\xd5', 230: u'\xb5', 231: u'\xfe', 232: u'\xde', 233: u'\xda', 234: u'\xdb', 235: u'\xd9', 
             236: u'\xfd', 237: u'\xdd', 238: u'\xaf', 239: u'\xb4', 240: u'\xad', 241: u'\xb1', 242: u'\u2017', 243: u'\xbe', 
             244: u'\xb6', 245: u'\xa7', 246: u'\xf7', 247: u'\xb8', 248: u'\xb0', 249: u'\xa8', 250: u'\xb7', 251: u'\xb9', 
             252: u'\xb3', 253: u'\xb2', 254: u'\u25a0', 255: u'\xa0'
             } ,
    862 :  { 128: u'\u05d0', 129: u'\u05d1', 130: u'\u05d2', 131: u'\u05d3', 132: u'\u05d4', 133: u'\u05d5', 134: u'\u05d6', 
             135: u'\u05d7', 136: u'\u05d8', 137: u'\u05d9', 138: u'\u05da', 139: u'\u05db', 140: u'\u05dc', 141: u'\u05dd', 
             142: u'\u05de', 143: u'\u05df', 144: u'\u05e0', 145: u'\u05e1', 146: u'\u05e2', 147: u'\u05e3', 148: u'\u05e4', 
             149: u'\u05e5', 150: u'\u05e6', 151: u'\u05e7', 152: u'\u05e8', 153: u'\u05e9', 154: u'\u05ea', 155: u'\xa2', 
             156: u'\xa3', 157: u'\xa5', 158: u'\u20a7', 159: u'\u0192', 160: u'\xe1', 161: u'\xed', 162: u'\xf3', 163: u'\xfa', 
             164: u'\xf1', 165: u'\xd1', 166: u'\xaa', 167: u'\xba', 168: u'\xbf', 169: u'\u2310', 170: u'\xac', 171: u'\xbd', 
             172: u'\xbc', 173: u'\xa1', 174: u'\xab', 175: u'\xbb', 176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 
             180: u'\u2524', 181: u'\u2561', 182: u'\u2562', 183: u'\u2556', 184: u'\u2555', 185: u'\u2563', 186: u'\u2551', 
             187: u'\u2557', 188: u'\u255d', 189: u'\u255c', 190: u'\u255b', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 
             194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 197: u'\u253c', 198: u'\u255e', 199: u'\u255f', 200: u'\u255a', 
             201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\u2567', 
             208: u'\u2568', 209: u'\u2564', 210: u'\u2565', 211: u'\u2559', 212: u'\u2558', 213: u'\u2552', 214: u'\u2553', 
             215: u'\u256b', 216: u'\u256a', 217: u'\u2518', 218: u'\u250c', 219: u'\u2588', 220: u'\u2584', 221: u'\u258c', 
             222: u'\u2590', 223: u'\u2580', 224: u'\u03b1', 225: u'\xdf', 226: u'\u0393', 227: u'\u03c0', 228: u'\u03a3', 
             229: u'\u03c3', 230: u'\xb5', 231: u'\u03c4', 232: u'\u03a6', 233: u'\u0398', 234: u'\u03a9', 235: u'\u03b4', 
             236: u'\u221e', 237: u'\u03c6', 238: u'\u03b5', 239: u'\u2229', 240: u'\u2261', 241: u'\xb1', 242: u'\u2265', 
             243: u'\u2264', 244: u'\u2320', 245: u'\u2321', 246: u'\xf7', 247: u'\u2248', 248: u'\xb0', 249: u'\u2219', 
             250: u'\xb7', 251: u'\u221a', 252: u'\u207f', 253: u'\xb2', 254: u'\u25a0', 255: u'\xa0'
             } ,
    737 :  { 128: u'\u0391', 129: u'\u0392', 130: u'\u0393', 131: u'\u0394', 132: u'\u0395', 133: u'\u0396', 134: u'\u0397', 
             135: u'\u0398', 136: u'\u0399', 137: u'\u039a', 138: u'\u039b', 139: u'\u039c', 140: u'\u039d', 141: u'\u039e', 
             142: u'\u039f', 143: u'\u03a0', 144: u'\u03a1', 145: u'\u03a3', 146: u'\u03a4', 147: u'\u03a5', 148: u'\u03a6', 
             149: u'\u03a7', 150: u'\u03a8', 151: u'\u03a9', 152: u'\u03b1', 153: u'\u03b2', 154: u'\u03b3', 155: u'\u03b4', 
             156: u'\u03b5', 157: u'\u03b6', 158: u'\u03b7', 159: u'\u03b8', 160: u'\u03b9', 161: u'\u03ba', 162: u'\u03bb', 
             163: u'\u03bc', 164: u'\u03bd', 165: u'\u03be', 166: u'\u03bf', 167: u'\u03c0', 168: u'\u03c1', 169: u'\u03c3', 
             170: u'\u03c2', 171: u'\u03c4', 172: u'\u03c5', 173: u'\u03c6', 174: u'\u03c7', 175: u'\u03c8', 176: u'\u2591', 
             177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\u2561', 182: u'\u2562', 183: u'\u2556', 
             184: u'\u2555', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\u255c', 190: u'\u255b', 
             191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 197: u'\u253c', 
             198: u'\u255e', 199: u'\u255f', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 204: u'\u2560', 
             205: u'\u2550', 206: u'\u256c', 207: u'\u2567', 208: u'\u2568', 209: u'\u2564', 210: u'\u2565', 211: u'\u2559', 
             212: u'\u2558', 213: u'\u2552', 214: u'\u2553', 215: u'\u256b', 216: u'\u256a', 217: u'\u2518', 218: u'\u250c', 
             219: u'\u2588', 220: u'\u2584', 221: u'\u258c', 222: u'\u2590', 223: u'\u2580', 224: u'\u03c9', 225: u'\u03ac', 
             226: u'\u03ad', 227: u'\u03ae', 228: u'\u03ca', 229: u'\u03af', 230: u'\u03cc', 231: u'\u03cd', 232: u'\u03cb', 
             233: u'\u03ce', 234: u'\u0386', 235: u'\u0388', 236: u'\u0389', 237: u'\u038a', 238: u'\u038c', 239: u'\u038e', 
             240: u'\u038f', 241: u'\xb1', 242: u'\u2265', 243: u'\u2264', 244: u'\u03aa', 245: u'\u03ab', 246: u'\xf7', 
             247: u'\u2248', 248: u'\xb0', 249: u'\u2219', 250: u'\xb7', 251: u'\u221a', 252: u'\u207f', 253: u'\xb2', 
             254: u'\u25a0', 255: u'\xa0'
             } ,
    437 :  { 128: u'\xc7', 129: u'\xfc', 130: u'\xe9', 131: u'\xe2', 132: u'\xe4', 133: u'\xe0', 134: u'\xe5', 135: u'\xe7', 
             136: u'\xea', 137: u'\xeb', 138: u'\xe8', 139: u'\xef', 140: u'\xee', 141: u'\xec', 142: u'\xc4', 143: u'\xc5', 
             144: u'\xc9', 145: u'\xe6', 146: u'\xc6', 147: u'\xf4', 148: u'\xf6', 149: u'\xf2', 150: u'\xfb', 151: u'\xf9', 
             152: u'\xff', 153: u'\xd6', 154: u'\xdc', 155: u'\xa2', 156: u'\xa3', 157: u'\xa5', 158: u'\u20a7', 159: u'\u0192', 
             160: u'\xe1', 161: u'\xed', 162: u'\xf3', 163: u'\xfa', 164: u'\xf1', 165: u'\xd1', 166: u'\xaa', 167: u'\xba',
             168: u'\xbf', 169: u'\u2310', 170: u'\xac', 171: u'\xbd', 172: u'\xbc', 173: u'\xa1', 174: u'\xab', 175: u'\xbb',
             176: u'\u2591', 177: u'\u2592', 178: u'\u2593', 179: u'\u2502', 180: u'\u2524', 181: u'\u2561', 182: u'\u2562', 
             183: u'\u2556', 184: u'\u2555', 185: u'\u2563', 186: u'\u2551', 187: u'\u2557', 188: u'\u255d', 189: u'\u255c', 
             190: u'\u255b', 191: u'\u2510', 192: u'\u2514', 193: u'\u2534', 194: u'\u252c', 195: u'\u251c', 196: u'\u2500', 
             197: u'\u253c', 198: u'\u255e', 199: u'\u255f', 200: u'\u255a', 201: u'\u2554', 202: u'\u2569', 203: u'\u2566', 
             204: u'\u2560', 205: u'\u2550', 206: u'\u256c', 207: u'\u2567', 208: u'\u2568', 209: u'\u2564', 210: u'\u2565', 
             211: u'\u2559', 212: u'\u2558', 213: u'\u2552', 214: u'\u2553', 215: u'\u256b', 216: u'\u256a', 217: u'\u2518', 
             218: u'\u250c', 219: u'\u2588', 220: u'\u2584', 221: u'\u258c', 222: u'\u2590', 223: u'\u2580', 224: u'\u03b1', 
             225: u'\xdf', 226: u'\u0393', 227: u'\u03c0', 228: u'\u03a3', 229: u'\u03c3', 230: u'\xb5', 231: u'\u03c4', 
             232: u'\u03a6', 233: u'\u0398', 234: u'\u03a9', 235: u'\u03b4', 236: u'\u221e', 237: u'\u03c6', 238: u'\u03b5', 
             239: u'\u2229', 240: u'\u2261', 241: u'\xb1', 242: u'\u2265', 243: u'\u2264', 244: u'\u2320', 245: u'\u2321', 
             246: u'\xf7', 247: u'\u2248', 248: u'\xb0', 249: u'\u2219', 250: u'\xb7', 251: u'\u221a', 252: u'\u207f', 
             253: u'\xb2', 254: u'\u25a0', 255: u'\xa0'
             } ,
}

