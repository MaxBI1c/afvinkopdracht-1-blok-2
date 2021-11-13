def lezen_sequentie():
    training_bestand = "hamming_distance_training.fa"
    test_bestand = "hamming_distance_test.fa"
    open_training = open(opentraining_bestand, 'r')
    header_training = []
    sequentie_training = []
    open_test = open(training_bestand, 'r')
    header_test = []
    sequentie_test = []
    training = training_bestand.read
    test = test_bestand.read
def sequentie():
    aantal_a = count.sequentie_test('A')
    aantal_t = count.sequentie_test('T')
    aantal_c = count.sequentie_test('C')
    aantal_g = count.sequentie_test('G')
    aantal_A = [aantal_a]
    aantal_T = [aantal_t]
    aantal_c = [aantal_c]
    aantal_G = [aantal_g]
    
main()
    lezen_sequentie()
    sequentie()
main()
