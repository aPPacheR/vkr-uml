import Foundation

final class Branch {
    private let id: Int
    private let name: String
    private let address: String

    init(id: Int, name: String, address: String) {
        self.id = id
        self.name = name
        self.address = address
    }
}
