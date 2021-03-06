//https://mp.weixin.qq.com/s/A993f7N52DgS867XznfYxw


type Interface interface {
   // Len is the number of elements in the collection.
   Len() int
   // Less reports whether the element with
   // index i should sort before the element with index j.
   Less(i, j int) bool
   // Swap swaps the elements with indexes i and j.
   Swap(i, j int)
}


func heapSort(data Interface, a, b int) {
   first := a
   lo := 0
   hi := b - a

   // Build heap with greatest element at top.
   for i := (hi - 1) / 2; i >= 0; i-- {
       siftDown(data, i, hi, first)
   }
   // Pop elements, largest first, into end of data.
   for i := hi - 1; i >= 0; i-- {
       data.Swap(first, first+i)
       siftDown(data, lo, i, first)
   }
}


// siftDown implements the heap property on data[lo, hi).
// first is an offset into the array where the root of the heap lies.
func siftDown(data Interface, lo, hi, first int) {
   root := lo
   for {
        child := 2*root + 1
        if child >= hi {
            break
        }
        if child+1 < hi && data.Less(first+child, first+child+1) {
            child++
        }
        if !data.Less(first+root, first+child) {
            return
        }
        data.Swap(first+root, first+child)
        root = child
    }
}
