## Code Snippet

### file open
```python
f = open("input_file.txt", "r")
```
### file close

```python
f.close()
```

### 일반 파일 생성
```python
f = open("output_file.txt", "w")
```


### temp file 생성
현재 위치를 기준으로 temp directory에 랜덤 파일명의 temp file 생성
```python
tempFile = tempfile.NamedTemporaryFile(dir=self.cwd + '/temp', delete=False)
```

### file 포인터 이동
파일 끝까지 읽거나, 끝에다가 write 할 때 포인터가 마지막에 위치하게 되므로 다음에 파일을 읽을때 마지막 라인에서 읽거나/쓰기 시작함. <br/>따라서, 처음부터 읽거나 쓰고 싶을때는 seek(0)로 파일 처음으로 포인터를 이동.
```python
f.seek(0)
```

### file write
```python
# write multiple lines at once
f.writelines(list)

# write one line
f.write("writesomething\n")

```