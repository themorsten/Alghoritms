void Buble_sort(int* A, const int size) {
	int i = 0;
	bool t = true;
	while (t) {
		t = false;
		for (int j = 0; j < size - 1 - i; j++) {
			if (A[j] > A[j + 1]) {
				swap(A[j], A[j + 1]);
				t = true;
			}
		}
		i++;
	}
}
