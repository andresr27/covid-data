#! /usr/bin/python3
import re
import os
## Need this line so Atom can run it
os.chdir('/home/andres/Programs/python/covid/app/scripts')
path = 'data/base1.html' #html file location
new_path = 'data/base_new.html'
patterns = ['lib/']
     
for pattern in patterns:
    pat1 = 'href=\"'+ pattern
    pat2 = 'src=\"'+pattern

    with open(path) as txt, open(new_path, 'w') as out:
        print(str(txt))
        k = 0
        for oline in txt:
            print(str(k) + " " + oline)
            if k < 141:
                k += 1
            else: break
            if re.search(pat1, oline) or re.search(pat2, oline): # Don't recall why I put this.

                print (pat1 + pat2)
                if re.search(pat1, oline):
                    print("Original line for Href: " + str(oline))
                    line = oline.split(' ')
                    ref = line[3].split(pattern)
                    new_ref1 = "{{ url_for('static', filename='" + pattern + ref[1].strip('\"') + "') }}"
                    ref[1] = new_ref1
                    line[3] = ref[0] + ref[1] + "\""
                    new_line = ' '.join(line)
                    print("Flask formated line: " + new_line)
                    #txt.write(new_line)
                    out.write(new_line)

                elif re.search(pat2, oline):
                    print("Original line for src: " + str(oline))
                    line = oline.split('\"')
                    #print(str(line))
                    for i in range(len(line)):
                        if re.search(pattern, line[i]):
                            #print ("Element found")
                            break

                    ref = line[i].split(pattern)
                    #print(ref)
                    new_ref1 = "{{ url_for('static', filename='" + pattern + ref[1].strip('\"') + "') }}"
                    ref[1] = new_ref1
                    line[i] = ref[0] + ref[1]
                    new_line = '\"'.join(line)
                    print("Flask formated line: " + new_line)
                    #txt.write(new_line)
                    out.write(new_line)

            else:
                new_line = str(oline)
                #txt.write(new_line)
                out.write(new_line)

## Need to copy file to original path befor a can replace next patter else I'll changes for curretn pattern <- Did it manually for now
    # with open(path, 'w') as t:
    #     t.write(out)
