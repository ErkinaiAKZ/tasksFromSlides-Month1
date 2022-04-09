#№1

text = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
text2 = (text.split( ))
print(len(text2))

#№2

word = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
word2 = word.split()
for i in word2:
    print(type(word2), end=' ')
print('\n')

#№3

message ='хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(message.upper())

#№4

symbol = input('введите символ:')
name = 'GitHub'
print(symbol.join(name))


#№5
text = "Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
t = text.replace('е', '3')
print(t)


#№6

text = 'The Biden administration announced a plan to release around 1 million barrels of oil a day from the Strategic Petroleum Reserve for as long as six months.'

part1 = text[:len(text) // 2]
p1 = part1.lower()
part2 = text[len(text) // 2:]
p2 = part2.upper()

print(p1 + p2)

#№7

a = True
print(a)