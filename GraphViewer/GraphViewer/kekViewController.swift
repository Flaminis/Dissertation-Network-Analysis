//
//  kekViewController.swift
//  
//
//  Created by Yerbol Kopzhassar on 01/11/2016.
//
//

import UIKit
import SwiftyJSON
import Charts
class kekViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let mainGraph: UnweightedGraph<String> = UnweightedGraph<String>()
        var jsooon: DisserGraphml!
        
        if let path = Bundle.main.path(forResource: "GraphDisser", ofType: "json") {
            do {
                let data = try Data(contentsOf: URL(fileURLWithPath: path), options: .alwaysMapped)
                let jsonObj = JSON(data: data)
                if jsonObj != JSON.null {
                    print("jsonData:\(jsonObj)")
                    //                    let json = JSON(data: jsonObj as Data) // Note: data: parameter name
                    let graphs = DisserGraphml.init(json: jsonObj["graphml"])
                    print(jsonObj)
                    jsooon = graphs
                    print(graphs.graph?.node?.count)
                    mainGraph.addVertex("\(0)")
                    for nodee in (graphs.graph?.node)!{
                        print(nodee.internalIdentifier)
                        mainGraph.addVertex("\(Int(nodee.internalIdentifier!)!)")
                        let randomNumx:UInt32 = arc4random_uniform(100) // range is 0 to 99
                        let randomNumy:UInt32 = arc4random_uniform(100) // range is 0 to 99
                        
                        // convert the UInt32 to some other  types
                        
                        
                        let someIntx:Double = Double(randomNumx)
                        let someInty:Double = Double(randomNumy)
                        jsooon.graph?.node?[Int(nodee.internalIdentifier!)!-1].position_x = someIntx
                        jsooon.graph?.node?[Int(nodee.internalIdentifier!)!-1].position_y = someInty
                        
                    }
                    
                    for edge in (graphs.graph?.edge)!{
                        mainGraph.addEdge(from: Int(edge.source!)!, to: Int(edge.target!)!)
                    }
                    
                    //       drawGraph(mainGraph: mainGraph, jsonGraph: jsooon)
                } else {
                    print("Could not get json from file, make sure that file contains valid json.")
                }
            } catch let error {
                print(error.localizedDescription)
            }
        } else {
            print("Invalid filename/path.")
        }
        
        print(mainGraph)
        print(mainGraph.neighborsForVertex(String(2)))
        
//        repeat{
//            //jsooon = drawGraph(mainGraph: mainGraph, jsonGraph: jsooon)
//            
//            
//            
//        } while(true)
        
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    
    
    
    
    func drawGraph(mainGraph: UnweightedGraph<String>,jsonGraph: DisserGraphml) -> DisserGraphml{
        let restLenght = 10.0 //Длинна между точками
        let repulsiveForce = 1.0
        let springForce = 1.0
        let timeStepDelta = 1.0
        var distanceSquared = 0.0
        var distance = 0.0
        var force = 0.0
        var nodeNum = jsonGraph.graph?.node?.count
        var i = 0
        var fx = 0.0
        var fy = 0.0
        var newGraph = jsonGraph
        //repulsiya
        for i in 0...nodeNum!-1{ //-1 mb
            newGraph.graph?.node?[i].force_x = 0.0
            newGraph.graph?.node?[i].force_y = 0.0
        }
        var i1 = 0
        
        for i1 in 0...nodeNum!-2{
            var node1 = jsonGraph.graph?.node?[i1]
            
            for i2 in i1+1...nodeNum!-1{
                
                var node2 = jsonGraph.graph?.node?[i2]
                var dx = (node2?.position_x)! - (node1?.position_x)!
                var dy = (node2?.position_y)! - (node1?.position_y)!
                
                if (!(((dx < 0.1) && (dx > -0.1))) || !(((dy < 0.1) && (dy > -0.1)))){
                    distanceSquared = (dx*dx)+(dy*dy)
                    distance = sqrt(distanceSquared)
                    force = repulsiveForce/distanceSquared
                    fx = force * dx / distance
                    fy = force * dy / distance
                    newGraph.graph?.node?[i1].force_x = (node1?.force_x)! - fx
                    newGraph.graph?.node?[i1].force_y = (node1?.force_y)! - fy
                    newGraph.graph?.node?[i2].force_y = (node2?.force_y)! + fy
                    newGraph.graph?.node?[i2].force_x = (node1?.force_x)! + fy
                }
            }
        }
        for i1 in 0...nodeNum!-1{
            var node1 = jsonGraph.graph?.node?[i1]
            var sosedi = mainGraph.neighborsForIndex(i1).count-1
            if sosedi<0{
                sosedi = 0
            }
            for j in 0...(sosedi) {
                var i2 = mainGraph.neighborsForIndex(j).count
                var node2 = jsonGraph.graph?.node?[i2]
                if i1<i2{
                    var dx = (jsonGraph.graph?.node?[i2].position_x)! - (jsonGraph.graph?.node?[i1].position_x)!
                    var dy = (jsonGraph.graph?.node?[i2].position_y)! - (jsonGraph.graph?.node?[i2].position_y)!
                    if (!(((dx < 0.1) && (dx > -0.1))) || !(((dy < 0.1) && (dy > -0.1)))){
                        distance = sqrt((dx*dx) + (dy*dy))
                        force = springForce * (distance - restLenght)
                        var fx = force * dx / distance
                        var fy = force * dy / distance
                        newGraph.graph?.node?[i1].force_x = (node1?.force_x)! + fx
                        newGraph.graph?.node?[i1].force_y = (node1?.force_y)! + fy
                        newGraph.graph?.node?[i2].force_y = (node2?.force_y)! - fy
                        newGraph.graph?.node?[i2].force_x = (node1?.force_x)! - fy
                    }
                }
            }
        }
        var xarr = [Double]()
        var yarr = [Double]()
        var maxDisplacementSquared = 0.0
        for i in 0...nodeNum!-1{ //-1 mb
            var node = newGraph.graph?.node?[i]
            var dx = timeStepDelta * (node?.force_x)!
            var dy = timeStepDelta * (node?.force_y)!
            var displacementSquared = dx*dx + dy*dy
            
            if displacementSquared>maxDisplacementSquared{
                maxDisplacementSquared = displacementSquared
                let s = sqrt(maxDisplacementSquared/displacementSquared)
                dx = dx * s
                dy = dy * s
            }
            newGraph.graph?.node?[i].position_x = (jsonGraph.graph?.node?[i].position_x)! + dx
            newGraph.graph?.node?[i].position_y = (jsonGraph.graph?.node?[i].position_y)! + dy
            xarr.append((newGraph.graph?.node?[i].position_x)!)
            yarr.append((newGraph.graph?.node?[i].position_y)!)
            print("for node: \(i)\n")
            print("old xy: \((jsonGraph.graph?.node?[i].position_x!)!) - \((jsonGraph.graph?.node?[i].position_y!)!) new xy \((newGraph.graph?.node?[i].position_x!)!)  - \((newGraph.graph?.node?[i].position_y!)!)")
            
            
        }
        setChart(xarr: xarr, yarr: yarr)
        return newGraph
        
        
    }
    func setChart(xarr: [Double], yarr: [Double]){
        
        var dataEntries: [ChartDataEntry] = []
        var k = 0
        for i in 0...xarr.count-1 {
            k = i
            if k==0{
                k = 1
            }
            let dataEntry = ChartDataEntry(x: xarr[k], y: yarr[k])
            dataEntries.append(dataEntry)
        }
        let lineChartDataSet = LineChartDataSet(values: dataEntries, label: "Units Sold")
        
        let lineChartData = LineChartData(dataSet: lineChartDataSet)
        
        //        lineChartView = LineChartView(frame: CGRect(x: 0, y: 0, width: 480, height: 350))
        
        //   lineChartView.data = lineChartData
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}

