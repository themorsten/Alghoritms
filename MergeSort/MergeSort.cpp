void Merge(int* A, int left,int mid, int right) {
	int* c = new int[right - left + 1];
	int it1 = left, it2 = mid + 1,i=0;
	while (it1 <= mid || it2 <= right) {
		if (it2>right ||(it1<= mid && A[it1]<A[it2])) {
			c[i++] = A[it1++];
		}
		else {
			c[i++] = A[it2++];
		}
	}
	for (i = 0; i < right - left + 1; i++) A[left + i] = c[i];
	delete[]c;
}

void MergeSort(int* A, int left, int right) {
	if (left<right) {
		int m = (right + left) / 2;
		MergeSort(A, left, m);
		MergeSort(A, m + 1, right);
		Merge(A, left,m, right);
	}
}
