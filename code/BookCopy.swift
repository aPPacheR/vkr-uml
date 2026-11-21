import Foundation

final class BookCopy {
    private let id: Int
    private let isAvailable: Bool

    init(id: Int, isAvailable: Bool) {
        self.id = id
        self.isAvailable = isAvailable
    }
}
