https://www.jianshu.com/p/208c15226baf
```go
if info.OnlineRsp.Body != nil {
     // info.OnlineRsp.Body是包含了Reader 和Closer 这两接口的一个接口
		reader, err := gzip.NewReader(info.OnlineRsp.Body)
     // 返回Reader结构体


func NewDecoder(r io.Reader) *Decoder {
	return &Decoder{r: r}
}
type Decoder struct {
	r       io.Reader
	...
} 
// json.NewDecoder传入实现了io.Reader接口的struct，返回Decoder struct
// Decoder struct 有Decode方法
dec := json.NewDecoder(reader)


err = dec.Decode(&onlineResult)
```
