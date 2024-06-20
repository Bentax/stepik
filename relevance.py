### Нам пришел запрос с признаками (1,1). Отсортируйте документы в порядке убывания релевантности относительно данного запроса.

def relevance(q, d):
	return -(q[0] - d[0])**2 - 2*((q[1] - d[1])**2)

docs = [
	(0.0, 1.0),
	(1.0, 0.0),
	(1.0, 0.5),
]

q = (1, 1)

for doc in docs:
	print("relevance", relevance(q, doc))

###
def relevance(q, d):
    return -(q[0] - d[0])**2 - 2*((q[1] - d[1])**2)

docs = [[0.0, 1.0],
        [1.0, 0.0],
        [1.0, 0.5]
]
q = [1, 1]

res = []
for idx, doc in enumerate(docs):
    print(idx+1, relevance(q, doc))
    res.append([idx+1, relevance(q, doc)])
    
res.sort(key=lambda x: x[1], reverse=True)
print(res)
