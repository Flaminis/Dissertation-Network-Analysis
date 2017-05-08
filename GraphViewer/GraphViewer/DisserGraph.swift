//
//  DisserGraph.swift
//
//  Created by Yerbol Kopzhassar on 31/10/2016
//  Copyright (c) . All rights reserved.
//

import Foundation
import SwiftyJSON

public struct DisserGraph {

  // MARK: Declaration for string constants to be used to decode and also serialize.
  private let kDisserGraphNodeKey: String = "node"
  private let kDisserGraphInternalIdentifierKey: String = "id"
  private let kDisserGraphEdgedefaultKey: String = "edgedefault"
  private let kDisserGraphEdgeKey: String = "edge"

  // MARK: Properties
  public var node: [DisserNode]?
  public var internalIdentifier: String?
  public var edgedefault: String?
  public var edge: [DisserEdge]?

  // MARK: SwiftyJSON Initalizers
  /**
   Initates the instance based on the object
   - parameter object: The object of either Dictionary or Array kind that was passed.
   - returns: An initalized instance of the class.
  */
  public init(object: Any) {
    self.init(json: JSON(object))
  }

  /**
   Initates the instance based on the JSON that was passed.
   - parameter json: JSON object from SwiftyJSON.
   - returns: An initalized instance of the class.
  */
  public init(json: JSON) {
    if let items = json[kDisserGraphNodeKey].array { node = items.map { DisserNode(json: $0) } }
    internalIdentifier = json[kDisserGraphInternalIdentifierKey].string
    edgedefault = json[kDisserGraphEdgedefaultKey].string
    if let items = json[kDisserGraphEdgeKey].array { edge = items.map { DisserEdge(json: $0) } }
  }

  /**
   Generates description of the object in the form of a NSDictionary.
   - returns: A Key value pair containing all valid values in the object.
  */
  public func dictionaryRepresentation() -> [String: Any] {
    var dictionary: [String: Any] = [:]
    if let value = node { dictionary[kDisserGraphNodeKey] = value.map { $0.dictionaryRepresentation() } }
    if let value = internalIdentifier { dictionary[kDisserGraphInternalIdentifierKey] = value }
    if let value = edgedefault { dictionary[kDisserGraphEdgedefaultKey] = value }
    if let value = edge { dictionary[kDisserGraphEdgeKey] = value.map { $0.dictionaryRepresentation() } }
    return dictionary
  }

}
