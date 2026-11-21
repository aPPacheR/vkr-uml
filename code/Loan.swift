import Foundation

final class Loan {
    private let id: Int
    private let dueDate: String

    init(id: Int, dueDate: String) {
        self.id = id
        self.dueDate = dueDate
    }
}
