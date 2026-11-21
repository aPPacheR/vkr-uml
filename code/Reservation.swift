import Foundation

final class Reservation {
    private let id: Int
    private let status: String

    init(id: Int, status: String) {
        self.id = id
        self.status = status
    }

    func cancel() {
        fatalError("not implemented")
    }
}
