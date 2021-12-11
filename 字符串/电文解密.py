lsc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
lsp = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'

plaintext = ''
ciphertext = input()
for a in ciphertext:
    try:
        plaintext = plaintext + lsc[lsp.index(a)]
    except:
        plaintext = plaintext + a
print(plaintext)