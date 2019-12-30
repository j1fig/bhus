package bhus

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class OperatorVehicles extends Simulation {
    val feeder = jsonFile("operator_vehicles.json").random

    val httpProtocol = http
      .baseUrl("http://localhost:8000")
      .acceptHeader("application/json")
      .userAgentHeader("Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0")

    val scn = scenario("OperatorVehicles")
      .feed(feeder)
      .exec(http("operator_vehicles")
        .get("/api/operator/${operator_id}/vehicle?from=${from}&to=${to}")
      )

    // read https://gatling.io/docs/current/general/simulation_setup#injection
    // before modifying.
    setUp(
      scn.inject(
        nothingFor(5 seconds),
        rampUsersPerSec(1) to(600) during(3 minutes),
        constantUsersPerSec(600) during(2 minutes),
        rampUsersPerSec(600) to(1) during(3 minutes),
        nothingFor(5 seconds)
      )
    ).protocols(httpProtocol)
}
