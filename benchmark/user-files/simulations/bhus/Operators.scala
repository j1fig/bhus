package bhus

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class Operators extends Simulation {
    val feeder = jsonFile("operators.json").random

    val httpProtocol = http
      .baseUrl("http://localhost:8000")
      .acceptHeader("application/json")
      .userAgentHeader("Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0")

    val scn = scenario("Operators")
      .feed(feeder)
      .exec(http("operators")
        .get("/api/operator?from=${from}&to=${to}")
      )

    // read https://gatling.io/docs/current/general/simulation_setup#injection
    // before modifying.
    setUp(
      scn.inject(
        nothingFor(5 seconds),
        rampUsersPerSec(1) to(100) during(3 minutes),
        constantUsersPerSec(100) during(2 minutes),
        rampUsersPerSec(100) to(1) during(3 minutes),
        nothingFor(5 seconds)
      )
    ).protocols(httpProtocol)
}
