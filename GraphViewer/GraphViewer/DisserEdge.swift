//
//  DisserEdge.swift
//
//  Created by Yerbol Kopzhassar on 31/10/2016
//  Copyright (c) . All rights reserved.
//

import Foundation
import SwiftyJSON

public struct DisserEdge {

  // MARK: Declaration for string constants to be used to decode and also serialize.
  private let kDisserEdgeTargetKey: String = "target"
  private let kDisserEdgeSourceKey: String = "source"
  private let kDisserEdgeInternalIdentifierKey: String = "id"
  private let kDisserEdgeDirectedKey: String = "directed"

  // MARK: Properties
  public var target: String?
  public var source: String?
  public var internalIdentifier: String?
  public var directed: String?

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
    target = json[kDisserEdgeTargetKey].string
    source = json[kDisserEdgeSourceKey].string
    internalIdentifier = json[kDisserEdgeInternalIdentifierKey].string
    directed = json[kDisserEdgeDirectedKey].string
  }

  /**
   Generates description of the object in the form of a NSDictionary.
   - returns: A Key value pair containing all valid values in the object.
  */
  public func dictionaryRepresentation() -> [String: Any] {
    var dictionary: [String: Any] = [:]
    if let value = target { dictionary[kDisserEdgeTargetKey] = value }
    if let value = source { dictionary[kDisserEdgeSourceKey] = value }
    if let value = internalIdentifier { dictionary[kDisserEdgeInternalIdentifierKey] = value }
    if let value = directed { dictionary[kDisserEdgeDirectedKey] = value }
    return dictionary
  }

}
