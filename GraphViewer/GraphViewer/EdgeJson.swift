//
//  Node.swift
//  GraphViewer
//
//  Created by Yerbol Kopzhassar on 31/10/2016.
//  Copyright © 2016 Yerbol Kopzhassar. All rights reserved.
//

class EdgeJson {
    var id : Int!
    var source : String!
    var target: String!
    var directed: Bool!

    init(id: Int, source: String, target:String,directed:Bool){
        self.id = id
        self.source = source
        self.target = target
        self.directed = directed
    }
}
