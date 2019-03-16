from initdata import elliot, darling, tyrell
import pickle

for (key, record) in [('elliot', elliot),('darling',darling),('tyrell',tyrell)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump = (record, recfile)
    recfile.close()
