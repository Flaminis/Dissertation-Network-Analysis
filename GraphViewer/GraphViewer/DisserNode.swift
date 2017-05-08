//
//  DisserNode.swift
//
//  Created by Yerbol Kopzhassar on 31/10/2016
//  Copyright (c) . All rights reserved.
//

import Foundation
import SwiftyJSON

public struct DisserNode {

  // MARK: Declaration for string constants to be used to decode and also serialize.
  private let kDisserNodeInternalIdentifierKey: String = "id"

  // MARK: Properties
  public var internalIdentifier: String?
    public var force_x: Double? = 0.0
    public var force_y: Double? = 0.0
    public var position_x: Double? = 0.0
    public var position_y: Double? = 0.0
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
    internalIdentifier = json[kDisserNodeInternalIdentifierKey].string
  }

  /**
   Generates description of the object in the form of a NSDictionary.
   - returns: A Key value pair containing all valid values in the object.
  */
  public func dictionaryRepresentation() -> [String: Any] {
    var dictionary: [String: Any] = [:]
    if let value = internalIdentifier { dictionary[kDisserNodeInternalIdentifierKey] = value }
    return dictionary
  }

}
