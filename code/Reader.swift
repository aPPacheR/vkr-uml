import Foundation

final class Reader {
    private let id: Int
    private let fullName: String
    private let cardNumber: String

    init(id: Int, fullName: String, cardNumber: String) {
        self.id = id
        self.fullName = fullName
        self.cardNumber = cardNumber
    }

    func reserve(book: Book) -> Reservation {
        fatalError("not implemented")
    }

    func renew(loan: Loan) {
        fatalError("not implemented")
    }
}
