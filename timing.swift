var sum = 0
for e in 0..<30{
    sum = 0
    var x = [Int]()
        for i in 0...1000000{
            x.append(i);
        }
    var y = [Int]()
        for i in 0..<1000000-1{
            y.append(x[i]+x[i+1])
        }
        for i in stride(from:0, to:1000000, by: 100){
            sum += y[i]
        }
}
print(sum)
// whoo i am swift
