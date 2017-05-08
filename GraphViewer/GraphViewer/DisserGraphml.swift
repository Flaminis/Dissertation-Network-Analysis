//
//  DisserGraphml.swift
//
//  Created by Yerbol Kopzhassar on 31/11/2016
//  Copyright (c) . All rights reserved.
//

import Foundation
import SwiftyJSON

public struct DisserGraphml {

  // MARK: Declaration for string constants to be used to decode and also serialize.
  private let kDisserGraphmlGraphKey: String = "graph"
  private let kDisserGraphmlXmlnsKey: String = "xmlns"
  private let kDisserGraphmlXmlnsxsiKey: String = "xmlnsxsi"

  // MARK: Properties
  public var graph: DisserGraph?
  public var xmlns: String?
  public var xmlnsxsi: String?

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
    graph = DisserGraph(json: json[kDisserGraphmlGraphKey])
    xmlns = json[kDisserGraphmlXmlnsKey].string
    xmlnsxsi = json[kDisserGraphmlXmlnsxsiKey].string
  }

  /**
   Generates description of the object in the form of a NSDictionary.
   - returns: A Key value pair containing all valid values in the object.
  */
  public func dictionaryRepresentation() -> [String: Any] {
    var dictionary: [String: Any] = [:]
    if let value = graph { dictionary[kDisserGraphmlGraphKey] = value.dictionaryRepresentation() }
    if let value = xmlns { dictionary[kDisserGraphmlXmlnsKey] = value }
    if let value = xmlnsxsi { dictionary[kDisserGraphmlXmlnsxsiKey] = value }
    return dictionary
  }

}
