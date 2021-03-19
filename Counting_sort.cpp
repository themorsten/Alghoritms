void Counting_sort(int* A, const int size,int k) {
	int* tmp = new int[k];
	for (int i = 0; i < k; i++) tmp[i] = 0;
	for (int i = 0; i < size; i++) tmp[A[i]]++;
	int pos = 0;
	for (int number = 0; number < k; number++) {
		for (int i = 0; i < tmp[number]; i++) {
			A[pos] = number;
			pos++;
		}
	}
	delete[]tmp;
}
