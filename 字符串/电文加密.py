lsc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
lsp = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
plaintext = input()
ciphertext = ''
for a in plaintext:
    try:
        ciphertext = ciphertext + lsp[lsc.index(a)]
    except:
        ciphertext = ciphertext + a
    print(ciphertext)