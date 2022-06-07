# Katta-kichik
# Sonlar ustida amallarning eng muximlaridan biri bu - taqqoslashdir. Ushbu masalada sizga qo'yilgan talab, ikkita butun sonni taqqoslash kerak bo'ladi

# Kiruvchi ma'lumotlar:
# Kirish oqimida ikkita butun son A va B berilgan bo'ladi, va ularning absolyut qiymati 2×109 dan kichik bo'ladi

# Chiquvchi ma'lumotlar:
# Chiqarish oqimida bitta belgi chiqarish kerak. Agar A > B bo'lsa ">", agar A = B bo'lsa "=", yoki A < B bo'lganda "<" belgisini.
[a,b] =list(map(int, input().split(" ")))
if a<b:
    print("<")
elif a>b:
    print(">") 
else:
    print("=")


