#ifndef READER_H
#define READER_H

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "orc/OrcFile.hh"

#include "Converter.h"
#include "TypeDescription.h"

namespace py = pybind11;

class ORCFileLikeObject
{
  private:
    py::object convertTimestampMillis(int64_t) const;

  protected:
    uint64_t batchItem;
    orc::RowReaderOptions rowReaderOpts;
    std::unique_ptr<orc::RowReader> rowReader;
    std::unique_ptr<orc::ColumnVectorBatch> batch;
    std::unique_ptr<Converter> converter;
    py::dict convDict;
    py::dict buildStatistics(const orc::Type*, const orc::ColumnStatistics*) const;
    const orc::Type* findColumnType(const orc::Type*, uint64_t) const;

  public:
    uint64_t currentRow;
    uint64_t firstRowOfStripe;
    virtual uint64_t len() const = 0;
    py::object next();
    py::list read(int64_t = -1);
    uint64_t seek(int64_t, uint16_t = 0);
    const orc::RowReaderOptions getRowReaderOptions() const { return rowReaderOpts; };
    const py::dict getConverterDict() const { return convDict; }
};

class Stripe; /* Forward declaration */

class Reader : public ORCFileLikeObject
{
  private:
    std::unique_ptr<orc::Reader> reader;
    uint64_t batchSize;
    unsigned int structKind;

  public:
    Reader(py::object,
           uint64_t = 1024,
           std::list<uint64_t> = {},
           std::list<std::string> = {},
           unsigned int = 0,
           py::object = py::none());
    uint64_t len() const override;
    uint64_t numberOfStripes() const;
    TypeDescription schema();
    TypeDescription selectedSchema();
    Stripe readStripe(uint64_t);
    py::tuple statistics(uint64_t);

    const orc::Reader& getORCReader() const { return *reader; }
    const uint64_t getBatchSize() const { return batchSize; }
    const unsigned int getStructKind() const { return structKind; }
};

class Stripe : public ORCFileLikeObject
{
  private:
    uint64_t stripeIndex;
    std::unique_ptr<orc::StripeInformation> stripeInfo;
    const Reader& reader;

  public:
    Stripe(const Reader&, uint64_t, std::unique_ptr<orc::StripeInformation>);
    py::tuple bloomFilterColumns();
    uint64_t len() const override;
    uint64_t length() const;
    uint64_t offset() const;
    py::tuple statistics(uint64_t);
    std::string writerTimezone();
};

#endif